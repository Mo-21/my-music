from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('genres', views.GenreMixin)
router.register('artists', views.ArtistMixin)
router.register('songs', views.SongViewSet, basename='songs')
router.register(
    'songs_with_new_artist',
    views.SongWithNewArtistMixin,
    basename='songs_with_new_artist'
)

urlpatterns = router.urls
