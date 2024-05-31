from django.contrib.auth import get_user_model
from rest_framework import status
from model_bakery import baker
from music.models import Artist
import pytest


User = get_user_model()


@pytest.mark.django_db
class TestArtists:
    def test_get_artists_return_401_if_user_is_not_authenticated(self, api_client):
        response = api_client.get('/music/artists/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_artists_return_200_if_user_is_authenticated(self, api_client, authenticate_user):
        authenticate_user(user=User)

        response = api_client.get('/music/artists/')

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_artist_return_401_if_user_is_not_authenticated(self, api_client):
        artist = baker.make(Artist)

        response = api_client.get(f'/music/artists/{artist.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_retrieve_artist_return_200_if_user_is_authenticated(self, api_client, authenticate_user):
        artist = baker.make(Artist)
        authenticate_user(user=User)

        response = api_client.get(f'/music/artists/{artist.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_create_artist_return_405_if_user_is_authenticated(self, api_client, authenticate_user):
        authenticate_user(user=User)

        response = api_client.post('/music/artists/', {'name': 'Rock'})

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
