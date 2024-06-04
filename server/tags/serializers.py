from rest_framework import serializers
from .models import Tag, TaggedItem


class TaggedItemSerializer(serializers.ModelSerializer):
    tag_id = serializers.IntegerField()

    class Meta:
        model = TaggedItem
        fields = ['tag_id', 'content_type', 'object_id']


class TagSerializer(serializers.ModelSerializer):
    tagged_items = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'label', 'tagged_items']
