from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'content_type', 'object_id', 'created_at', 'user']
        read_only_fields = ['created_at', 'user']

    def create(self, validated_data):
        user_id = self.context['user_id']
        content_type = validated_data['content_type']
        object_id = validated_data['object_id']

        if Like.objects.filter(user_id=user_id, content_type=content_type, object_id=object_id).exists():
            raise serializers.ValidationError('You already liked this object')

        like = Like.objects.create(user_id=user_id, **validated_data)
        return like
