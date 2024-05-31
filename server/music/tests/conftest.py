from rest_framework.test import APIClient
import pytest


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate_user(api_client):
    def do_authenticate_user(user):
        api_client.force_authenticate(user=user)
    return do_authenticate_user
