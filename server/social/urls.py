from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()

router.register('customers', views.CustomerViewSet)
router.register('posts', views.PostViewSet, basename='posts')
router.register('followers', views.FollowerViewSet)

posts_router = routers.NestedDefaultRouter(
    router, 'posts', lookup='post'
)
posts_router.register(
    'comments', views.CommentViewSet, basename='post-comments'
)
posts_router.register(
    'likes', views.LikeMixin, basename='post-likes'
)

urlpatterns = router.urls + posts_router.urls
