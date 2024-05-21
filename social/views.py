from rest_framework.viewsets import ModelViewSet
from .serializers import PersonSerializer, PostSerializer
from .models import Person, Post

# TODO: List only accessible for admins


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
