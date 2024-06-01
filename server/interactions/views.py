from rest_framework.viewsets import ModelViewSet
from .models import Like, Comment
from .serializers import LikeSerializer, CommentSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
