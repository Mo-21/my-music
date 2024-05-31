from django_filters.rest_framework import FilterSet
from .models import Song


class SongFilter(FilterSet):
    class Meta:
        model = Song
        fields = {
            'title': ['icontains'],
            'genre__name': ['icontains'],
            'artist__name': ['icontains'],
        }
