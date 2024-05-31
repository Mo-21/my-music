from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination
from .filters import SongFilter
from .models import Genre, Artist, Song, Playlist, PlaylistItem
from .serializers import (GenreSerializer, ArtistSerializer, SongSerializer, SongWithNewArtistSerializer,
                          PlaylistSerializer, PlaylistItemSerializer)


class GenreMixin(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name']


class ArtistMixin(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name']


class SongViewSet(ModelViewSet):
    queryset = Song.objects.select_related(
        'genre').select_related('artist').all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created_at']
    filterset_class = SongFilter

    def get_serializer_context(self):
        user = self.request.user

        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return {'user_id': user.id}


class SongWithNewArtistMixin(CreateModelMixin, GenericViewSet):
    serializer_class = SongWithNewArtistSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        user = self.request.user

        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return {'user_id': user.id}


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        user = self.request.user

        if not user.is_authenticated:
            raise NotAuthenticated('User is not authenticated')

        return {'user_id': user.id}


class PlaylistItemViewSet(ModelViewSet):
    queryset = PlaylistItem.objects.all()
    serializer_class = PlaylistItemSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'playlist_id': self.kwargs['playlist_pk']}
