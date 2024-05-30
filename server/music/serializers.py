from rest_framework import serializers
from .models import Genre, Artist, Song, Playlist, PlaylistItem


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'created_at']


class SongSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'user_id', 'duration',
                  'item', 'genre', 'artist', 'created_at']

    def create(self, validated_data):
        song = Song.objects.create(
            author_id=self.context['user_id'],
            **validated_data
        )

        return song


class SongWithNewArtistSerializer(SongSerializer):
    artist = ArtistSerializer()

    def create(self, validated_data):
        artist_data = validated_data.pop('artist')
        artist = Artist.objects.create(**artist_data)

        song = Song.objects.create(
            author_id=self.context['user_id'],
            artist=artist,
            **validated_data
        )

        return song


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'created_at', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        playlist = Playlist.objects.create(
            user_id=self.context['user_id'],
            **validated_data
        )

        return playlist


class PlaylistItemSerializer(serializers.ModelSerializer):
    song_id = serializers.IntegerField()

    def validate_song_id(self, value):
        if not Song.objects.filter(pk=value).exists():
            raise serializers.ValidationError('Song does not exist')
        return value

    def create(self, validated_data):
        song_id = validated_data['song_id']
        playlist_id = self.context['playlist_id']

        if PlaylistItem.objects.filter(playlist_id=playlist_id, song_id=song_id).exists():
            raise serializers.ValidationError(
                'Song already exists in the playlist'
            )

        playlist_item = PlaylistItem.objects.create(
            playlist_id=playlist_id,
            **validated_data
        )

        return playlist_item

    class Meta:
        model = PlaylistItem
        fields = ['id', 'playlist', 'song_id']
        read_only_fields = ['playlist']
