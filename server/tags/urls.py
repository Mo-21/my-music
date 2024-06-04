from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('tags', views.TagViewSet)
router.register('tagged_items', views.TaggedItemViewSet,
                basename='tagged_items')

urlpatterns = router.urls
