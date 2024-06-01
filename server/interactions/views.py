from rest_framework.viewsets import ModelViewSet
from .models import Like
from .serializers import LikeSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
