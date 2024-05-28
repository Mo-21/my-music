from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import CustomerViewSet


router = DefaultRouter()
router.register('customers', CustomerViewSet)

urlpatterns = router.urls
