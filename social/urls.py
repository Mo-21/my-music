from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import PersonViewSet


router = DefaultRouter()
router.register('user', PersonViewSet)

urlpatterns = router.urls
