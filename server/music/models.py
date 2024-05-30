from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.SmallIntegerField()
    item = models.FileField(upload_to='music/songs', validators=[
                            FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class PlaylistItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.PROTECT)
    song = models.ForeignKey(Song, on_delete=models.PROTECT)

    class Meta:
        unique_together = [['playlist', 'song']]
