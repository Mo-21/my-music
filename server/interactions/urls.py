from rest_framework.routers import DefaultRouter
from .views import LikeViewSet, CommentViewSet

router = DefaultRouter()
router.register('likes', LikeViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
