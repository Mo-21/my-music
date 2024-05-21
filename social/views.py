from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer, PostSerializer
from .models import Customer, Post

# TODO: List only accessible for admins


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
