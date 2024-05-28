from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import CustomerSerializer, PostSerializer
from .models import Customer, Post


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.prefetch_related('user').all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
