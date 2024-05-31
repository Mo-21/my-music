from django.contrib.auth import get_user_model
from rest_framework import status
from model_bakery import baker
import pytest

User = get_user_model()


@pytest.mark.django_db
class TestPlaylists:
    def test_get_playlists_return_401_if_user_is_not_authenticated(self, api_client):
        response = api_client.get('/music/playlists/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_playlists_return_200_if_user_is_authenticated(self, api_client, authenticate_user):
        authenticate_user(user=User)

        response = api_client.get('/music/playlists/')

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_playlist_return_401_if_user_is_not_authenticated(self, api_client):
        playlist = baker.make('music.Playlist')

        response = api_client.get(f'/music/playlists/{playlist.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_retrieve_playlist_return_200_if_user_is_authenticated(self, api_client, authenticate_user):
        playlist = baker.make('music.Playlist')
        authenticate_user(user=User)

        response = api_client.get(f'/music/playlists/{playlist.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_create_playlist_return_401_if_user_is__not_authenticated(self, api_client, authenticate_user):
        response = api_client.post('/music/playlists/', {'name': 'Rock'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
