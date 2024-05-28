from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer,
    UserSerializer as BaseUserSerializer
)
from rest_framework import serializers
from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'username',
                  'password', 'password_confirm', 'first_name', 'last_name']

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError(
                {'password': 'Password fields didn\'t match.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
