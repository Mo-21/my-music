from rest_framework import status
from django.forms.models import model_to_dict
from model_bakery import baker
from social.models import Customer
import pytest


@pytest.mark.django_db
class TestCustomers:
    def test_get_all_customers_return_401_if_not_admin(self, api_client):
        response = api_client.get('/social/customers/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_all_customers_return_403_if_auth_but_not_admin(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)

        response = api_client.get('/social/customers/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_all_customers_return_200_if_admin(self, api_client, authenticate_user):
        authenticate_user(is_staff=True)

        response = api_client.get('/social/customers/')

        assert response.status_code == status.HTTP_200_OK

    def test_create_customer_return_401_if_not_auth(self, api_client, create_customer):
        customer = create_customer()

        response = api_client.post(
            '/social/customers/', model_to_dict(customer))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_customer_return_201_if_auth(self, api_client, create_customer, authenticate_user):
        customer = create_customer()

        authenticate_user()
        response = api_client.post(
            '/social/customers/', model_to_dict(customer))

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_customer_profile_return_401_if_not_auth(self, api_client, create_customer):
        customer = create_customer()

        response = api_client.get(f'/social/customers/{customer.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_customer_profile_return_200_if_auth(self, api_client, create_customer, authenticate_user):
        customer = create_customer()

        authenticate_user()
        response = api_client.get(f'/social/customers/{customer.id}/')

        assert response.status_code == status.HTTP_200_OK
