from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from model_bakery import baker
from social.models import Customer
import pytest

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_customer(authenticate_user):
    def do_create_customer(is_authenticated=False):
        user = baker.make(User)
        customer = Customer.objects.get(user=user)
        customer.birthdate = ''
        if is_authenticated:
            authenticate_user(user)
        return customer
    return do_create_customer


@pytest.fixture
def authenticate_user(api_client):
    def do_authenticate_user(user):
        api_client.force_authenticate(user=user)
    return do_authenticate_user
