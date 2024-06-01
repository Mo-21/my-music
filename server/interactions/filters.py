from django_filters.rest_framework import FilterSet
from .models import Like, Comment


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'object_id': ['exact'],
            'content_type': ['exact'],
        }


class LikeFilter(FilterSet):
    class Meta:
        model = Like
        fields = {
            'object_id': ['exact'],
            'content_type': ['exact'],
        }
