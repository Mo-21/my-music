from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .serializers import GenreSerializer, ArtistSerializer
from .models import Genre, Artist


class GenreMixin(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ArtistMixin(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(ModelViewSet):
    pass
