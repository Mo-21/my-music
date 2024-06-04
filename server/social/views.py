from django.db.models import Q, Count
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomPagination
from .serializers import CustomerSerializer, PostSerializer, FollowerSerializer, LikeSerializer
from .models import Customer, Post, Follower, Like, Comment


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.select_related('user').all()
    serializer_class = CustomerSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        elif self.action in ['retrieve', 'me']:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.select_related('user').get(
            user_id=request.user.id
        )
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        if user.is_superuser:
            return Post.objects \
                .select_related('author__user') \
                .all()

        customer = user.customer
        following_ids = Follower.objects.filter(
            follower_user=customer).values_list('following_user_id', flat=True)

        return Post.objects \
            .select_related('author__user') \
            .filter(Q(author=customer) | Q(author_id__in=following_ids)) \
            .annotate(likes_count=Count('likes')) \
            .annotate(comments_count=Count('comments')) \
            .prefetch_related('comments') \


    def get_serializer_context(self):
        user = self.request.user

        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return {'author_id': user.customer.id}


class FollowerViewSet(ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return Follower.objects.filter(follower_user=user.customer)

    def get_serializer_context(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')
        return {'follower_user_id': user.customer.id}


class LikeMixin(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            return Like.objects.filter(post=self.request.query_params.get('post_id'))
        return Like.objects.filter(user=self.request.user.customer)

    def get_serializer_context(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')
        return {'user_id': user.customer.id}
