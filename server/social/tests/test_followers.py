from rest_framework import status
import pytest


@pytest.mark.django_db
class TestFollower:
    def test_follow_user_return_401_if_user_is_not_auth(self, api_client):
        response = api_client.post('/social/followers/', data={})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_follow_user_return_400_if_user_is_auth_and_data_is_invalid(self, api_client, create_customer):
        create_customer(is_authenticated=True)

        response = api_client.post('/social/followers/', data={})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_follow_user_return_400_if_user_follows_himself(self, api_client, create_customer):
        customer = create_customer(is_authenticated=True)

        response = api_client.post(
            '/social/followers/', data={'following_user': customer.id})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_follow_user_return_201_if_user_is_auth_and_data_is_valid(self, api_client, create_customer):
        customer1 = create_customer(is_authenticated=True)
        customer2 = create_customer(is_authenticated=True)

        response = api_client.post(
            '/social/followers/', data={'following_user': customer1.id})

        assert response.status_code == status.HTTP_201_CREATED

    def test_unfollow_user_return_401_if_user_is_not_auth(self, api_client):
        response = api_client.delete('/social/followers/1/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unfollow_user_return_204_if_user_is_auth_and_data_is_valid(self, api_client, create_customer):
        customer1 = create_customer(is_authenticated=True)
        customer2 = create_customer(is_authenticated=True)
        relation = api_client.post(
            '/social/followers/',
            data={'following_user': customer1.id}
        )
        data = relation.json()
        relation_id = data['id']

        response = api_client.delete(f'/social/followers/{relation_id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT
