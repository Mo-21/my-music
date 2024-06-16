from django.db.models import Q, Prefetch, Count
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated
from rest_framework.filters import OrderingFilter
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomPagination
from .serializers import CustomerSerializer, PostSerializer, FollowerSerializer, LikeSerializer, CommentSerializer
from .models import Customer, Post, Follower, Like, Comment


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects \
        .select_related('user') \
        .prefetch_related(
            Prefetch('post_set', queryset=Post.objects.all(),
                     to_attr='authored_posts')
        )

    serializer_class = CustomerSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        elif self.action in ['retrieve', 'me']:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects \
            .select_related('user') \
            .prefetch_related(
                Prefetch('post_set', queryset=Post.objects.all(),
                         to_attr='authored_posts')
            ).get(user_id=request.user.id)

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
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at']

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        queryset = Post.objects.select_related('author__user')

        if user.is_superuser:
            return queryset
        else:
            customer = user.customer
            following_ids = Follower.objects.filter(
                follower_user=customer).values_list('following_user_id', flat=True)
            queryset = queryset.filter(
                Q(author=customer) | Q(author_id__in=following_ids))

        queryset = queryset.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comments', distinct=True)
        )

        queryset = queryset.prefetch_related('comments', 'likes')

        return queryset

    def get_serializer_context(self):
        user = self.request.user

        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return {'author_id': user.customer.id}


class FollowerViewSet(ModelViewSet):
    queryset = Follower.objects.select_related(
        'follower_user', 'following_user')

    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return Follower.objects.select_related('follower_user', 'following_user').filter(follower_user=user.customer)

    def get_serializer_context(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')
        return {'follower_user_id': user.customer.id}


class LikeMixin(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            return Like.objects.filter(post=self.kwargs['post_pk'])
        return Like.objects.filter(user=self.request.user.customer)

    def get_serializer_context(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')
        return {'user_id': user.customer.id, 'post_id': self.kwargs['post_pk']}


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            return Comment.objects.filter(post=self.kwargs['post_pk'])
        return Comment.objects.filter(user=self.request.user.customer)

    def get_serializer_context(self):
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')
        return {'user_id': user.customer.id, 'post_id': self.kwargs['post_pk']}
