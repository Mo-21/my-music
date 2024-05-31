from django.contrib.auth import get_user_model
from rest_framework import status
from model_bakery import baker
from music.models import Song
import pytest


User = get_user_model()


@pytest.mark.django_db
class TestSongs:
    def test_get_songs_return_401_if_user_is_not_authenticated(self, api_client):
        response = api_client.get('/music/songs/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_songs_return_200_if_user_is_authenticated(self, api_client, authenticate_user):
        authenticate_user(user=User)

        response = api_client.get('/music/songs/')

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_song_return_401_if_user_is_not_authenticated(self, api_client):
        song = baker.make(Song)

        response = api_client.get(f'/music/songs/{song.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_retrieve_song_return_200_if_user_is_authenticated(self, api_client, authenticate_user):
        song = baker.make(Song)
        authenticate_user(user=User)

        response = api_client.get(f'/music/songs/{song.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_create_song_return_401_if_user_is_not_authenticated(self, api_client):
        response = api_client.post('/music/songs/', {'title': 'Song'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_song_return_400_if_user_is_authenticated_but_data_is_invalid(self, api_client, authenticate_user):
        authenticate_user(user=User)

        response = api_client.post('/music/songs/', {'title': 'Song'})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
