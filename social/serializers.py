from rest_framework import serializers
from .models import Person, Post


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'user_id', 'phone', 'birthdate', 'membership_status']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'user', 'created_at']
