from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('genres', views.GenreMixin)
router.register('artists', views.ArtistMixin)

urlpatterns = router.urls
