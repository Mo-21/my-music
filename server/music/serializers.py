from rest_framework import serializers
from .models import Genre, Artist, Song


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'description']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'created_at']


class SongSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Song
        fields = ['title', 'user_id', 'duration',
                  'item', 'genre', 'artist', 'created_at']

    def create(self, validated_data):
        song = Song.objects.create(
            author_id=self.context['user_id'],
            **validated_data
        )

        return song
