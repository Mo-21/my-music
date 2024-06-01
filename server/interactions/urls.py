from rest_framework.routers import DefaultRouter
from .views import LikeViewSet

router = DefaultRouter()
router.register('likes', LikeViewSet)

urlpatterns = router.urls
