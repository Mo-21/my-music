from django.contrib.auth import get_user_model
from rest_framework import status
from model_bakery import baker
from music.models import Genre
import pytest

User = get_user_model()


@pytest.mark.django_db
class TestGenres:
    def test_get_genres_return_401_if_user_is_not_authenticated(self, api_client):
        response = api_client.get('/music/genres/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_genres_return_200_if_user_is_authenticated(self, api_client, authenticate_user):
        authenticate_user(user=User)

        response = api_client.get('/music/genres/')

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_genre_return_401_if_user_is_not_authenticated(self, api_client):
        genre = baker.make(Genre)

        response = api_client.get(f'/music/genres/{genre.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_retrieve_genre_return_200_if_user_is_authenticated(self, api_client, authenticate_user):
        genre = baker.make(Genre)
        authenticate_user(user=User)
        
        response = api_client.get(f'/music/genres/{genre.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_create_genre_return_405_if_user_is_authenticated(self, api_client, authenticate_user):
        authenticate_user(user=User)

        response = api_client.post('/music/genres/', {'name': 'Rock'})

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
