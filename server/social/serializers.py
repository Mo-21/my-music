from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer, Post, Follower, Comment


User = get_user_model()


class LocalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class CustomerSerializer(serializers.ModelSerializer):
    user = LocalUserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user', 'profile_image',
                  'phone', 'birthdate', 'membership_status']


class CommentSerializer(serializers.ModelSerializer):
    user = CustomerSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    author = CustomerSerializer(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'content', 'image',
                  'author', 'likes_count', 'comments_count', 
                  'comments', 'created_at']

    def create(self, validated_data):
        author_id = self.context['author_id']
        return Post.objects.create(author_id=author_id, **validated_data)


class FollowerSerializer(serializers.ModelSerializer):
    follower_user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Follower
        fields = ['id', 'follower_user', 'following_user']

    def create(self, validated_data):
        follower_user_id = self.context['follower_user_id']
        if follower_user_id == validated_data['following_user'].id:
            raise serializers.ValidationError('You cannot follow yourself')
        return Follower.objects.create(follower_user_id=follower_user_id, **validated_data)
