from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.exceptions import NotAuthenticated
from .serializers import GenreSerializer, ArtistSerializer, SongSerializer, SongWithNewArtistSerializer
from .models import Genre, Artist, Song


class GenreMixin(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ArtistMixin(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.select_related(
        'genre').select_related('artist').all()
    serializer_class = SongSerializer

    def get_serializer_context(self):
        user = self.request.user

        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return {'user_id': user.id}


class SongWithNewArtistMixin(CreateModelMixin, GenericViewSet):
    serializer_class = SongWithNewArtistSerializer

    def get_serializer_context(self):
        user = self.request.user

        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return {'user_id': user.id}
