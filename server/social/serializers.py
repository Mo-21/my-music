from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer, Post


User = get_user_model()


class LocalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class CustomerSerializer(serializers.ModelSerializer):
    user = LocalUserSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone', 'birthdate', 'membership_status']


class PostSerializer(serializers.ModelSerializer):
    author = CustomerSerializer()

    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'created_at']
