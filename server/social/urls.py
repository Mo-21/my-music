from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views


router = DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('posts', views.PostViewSet)

urlpatterns = router.urls
