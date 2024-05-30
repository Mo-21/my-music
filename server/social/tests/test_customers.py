from rest_framework import status
from django.forms.models import model_to_dict
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestCustomers:
    def test_get_all_customers_return_401_if_not_admin(self, api_client):
        response = api_client.get('/social/customers/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_all_customers_return_403_if_auth_but_not_admin(self, api_client, create_customer):
        create_customer(is_authenticated=True)

        response = api_client.get('/social/customers/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_customer_return_401_if_not_auth(self, api_client, create_customer):
        customer = create_customer()

        response = api_client.post(
            '/social/customers/', model_to_dict(customer))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_customer_return_403_if_auth(self, api_client, create_customer):
        customer = create_customer(is_authenticated=True)

        response = api_client.post(
            '/social/customers/', model_to_dict(customer))

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_customer_profile_return_401_if_not_auth(self, api_client, create_customer):
        customer = create_customer()

        response = api_client.get(f'/social/customers/{customer.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_customer_profile_return_200_if_auth(self, api_client, create_customer):
        customer = create_customer(is_authenticated=True)

        response = api_client.get(f'/social/customers/{customer.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_update_customer_return_401_if_not_auth(self, api_client, create_customer):
        customer = create_customer()
        url = reverse('customer-detail', kwargs={'pk': customer.id})
        data = {'phone': '987654321'}

        response = api_client.put(url, data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_customer_return_403_if_auth_but_not_same_user(self, api_client, create_customer):
        customer1 = create_customer(is_authenticated=True)
        customer2 = create_customer(is_authenticated=True)
        url = reverse('customer-detail', kwargs={'pk': customer1.id})
        data = {'phone': '987654321'}

        response = api_client.put(url, data)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_customer_return_200_if_same_user(self, api_client, create_customer):
        customer = create_customer(is_authenticated=True)
        url = reverse('customer-detail', kwargs={'pk': customer.id})
        data = {'phone': '987654321'}

        api_client.force_authenticate(user=customer.user)
        response = api_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK

    def test_delete_customer_return_401_if_not_auth(self, api_client, create_customer):
        customer = create_customer()
        url = reverse('customer-detail', kwargs={'pk': customer.id})

        response = api_client.delete(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_customer_return_403_if_auth_but_not_same_user(self, api_client, create_customer):
        customer1 = create_customer(is_authenticated=True)
        customer2 = create_customer(is_authenticated=True)
        url = reverse('customer-detail', kwargs={'pk': customer1.id})

        response = api_client.delete(url)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_customer_return_204_if_same_user(self, api_client, create_customer):
        customer = create_customer(is_authenticated=True)
        url = reverse('customer-detail', kwargs={'pk': customer.id})

        api_client.force_authenticate(user=customer.user)
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
