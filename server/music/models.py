from typing import Iterable
from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from mutagen import mp3, wave


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
    duration = models.SmallIntegerField(null=True, blank=True)
    item = models.FileField(upload_to='music/songs', validators=[
                            FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.item and not self.duration:
            if self.item.name.endswith('.mp3'):
                audio = mp3.MP3(self.item)
                self.duration = audio.info.length
            elif self.item.name.endswith('.wav'):
                audio = wave.Wave(self.item)
                self.duration = audio.info.length
        super().save(*args, **kwargs)


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
