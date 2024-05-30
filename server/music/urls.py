from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('genres', views.GenreMixin)
router.register('artists', views.ArtistMixin)
router.register('playlists', views.PlaylistViewSet)
router.register('songs', views.SongViewSet, basename='songs')
router.register(
    'songs_with_new_artist',
    views.SongWithNewArtistMixin,
    basename='songs_with_new_artist'
)

playlist_router = routers.NestedDefaultRouter(
    router, 'playlists', lookup='playlist'
)
playlist_router.register(
    'items', views.PlaylistItemViewSet, basename='playlist-items'
)

urlpatterns = router.urls + playlist_router.urls
