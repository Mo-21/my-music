from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from social.models import Customer
import pytest


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_customer_model(api_client):
    def do_create_customer_model():
        customer = baker.make(Customer)
        customer.birthdate = ''
        return customer
    return do_create_customer_model


@pytest.fixture
def create_customer(api_client, authenticate_user):
    def do_create_customer():
        customer = baker.make(Customer)
        customer.birthdate = ''

        authenticate_user(is_staff=True)

        api_client.post('/social/customers/', model_to_dict(customer))

        return customer
    return do_create_customer


@pytest.fixture
def create_user(api_client):
    def do_create_user():
        user = baker.make(User)
        api_client.post('/auth/users/', model_to_dict(user))
    return do_create_user


@pytest.fixture
def authenticate_user(api_client):
    def do_authenticate_user(is_staff=False):
        api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate_user
