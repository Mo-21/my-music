from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from .models import Tag, TaggedItem
from .serializers import TagSerializer, TaggedItemSerializer


class TagViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Tag.objects.prefetch_related('tagged_items').all()
    serializer_class = TagSerializer


class TaggedItemViewSet(ModelViewSet):
    serializer_class = TaggedItemSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            obj_type = self.request.query_params.get('obj_type')
            obj_id = self.request.query_params.get('obj_id')

            if not obj_type or not obj_id:
                raise ValidationError(
                    'obj_type and obj_id are required parameters.')

            try:
                model = ContentType.objects.get(model=obj_type).model_class()
            except ContentType.DoesNotExist:
                raise ValidationError('Invalid obj_type.')

            return TaggedItem.objects.get_tags_for(
                obj_type=model,
                obj_id=obj_id
            )
        return TaggedItem.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        obj_type = data.get('content_type')[0]
        obj_id = data.get('object_id')[0]
        tag_id = data.get('tag_id')[0]

        print(obj_type, obj_id, tag_id)

        if not obj_type or not obj_id or not tag_id:
            raise ValidationError(
                'obj_type, obj_id, and tag_id are required fields.')

        try:
            content_type = ContentType.objects.get(model='obj_type')
        except ContentType.DoesNotExist:
            raise ValidationError('Invalid obj_type.')

        tag = get_object_or_404(Tag, pk=tag_id)

        tagged_item = TaggedItem.objects.create(
            content_type=content_type,
            object_id=obj_id,
            tag=tag
        )

        serializer = self.get_serializer(tagged_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
