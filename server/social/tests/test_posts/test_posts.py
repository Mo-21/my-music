from django.forms.models import model_to_dict
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestPosts:
    def test_get_all_posts_return_401_if_not_auth(self, api_client):
        response = api_client.get('/social/posts/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_all_posts_return_200_if_auth(self, create_customer, api_client):
        create_customer(is_authenticated=True)

        response = api_client.get('/social/posts/')

        assert response.status_code == status.HTTP_200_OK

    def test_create_post_return_401_if_not_auth(self, api_client, create_post):
        post = create_post(is_authenticated=False)

        response = api_client.post('/social/posts/', model_to_dict(post))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_post_return_201_if_auth(self, api_client, create_post):
        post = create_post(is_authenticated=True)

        response = api_client.post('/social/posts/', model_to_dict(post))

        assert response.status_code == status.HTTP_201_CREATED

    def test_update_post_return_401_if_not_auth(self, api_client, create_post):
        post = create_post(is_authenticated=False)

        response = api_client.patch(
            f'/social/posts/{post.id}/', model_to_dict(post))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_post_return_404_if_not_owner_and_not_follower(self, api_client, create_post, create_customer):
        # users cannot even access posts from people they don't follow
        post = create_post(is_authenticated=True)
        customer = create_customer(is_authenticated=True)
        api_client.post('/social/posts/', model_to_dict(post))

        response = api_client.patch(
            f'/social/posts/{post.id}/', model_to_dict(post))

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_post_return_200_if_owner(self, api_client, create_post):
        post = create_post(is_authenticated=True)
        api_client.post('/social/posts/', model_to_dict(post))

        response = api_client.patch(
            f'/social/posts/{post.id}/', model_to_dict(post))

        assert response.status_code == status.HTTP_200_OK

    def test_delete_post_return_401_if_not_auth(self, api_client, create_post):
        post = create_post(is_authenticated=False)

        response = api_client.delete(f'/social/posts/{post.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_post_return_404_if_not_owner_and_not_follower(self, api_client, create_post, create_customer):
        post = create_post(is_authenticated=True)
        customer = create_customer(is_authenticated=True)
        api_client.post('/social/posts/', model_to_dict(post))

        response = api_client.delete(f'/social/posts/{post.id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_post_return_204_if_owner(self, api_client, create_post):
        post = create_post(is_authenticated=True)
        api_client.post('/social/posts/', model_to_dict(post))

        response = api_client.delete(f'/social/posts/{post.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT
