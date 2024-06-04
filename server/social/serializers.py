from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Customer, Post, Follower, Comment, Like


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


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['created_at', 'user']

    def create(self, validated_data):
        customer_id = self.context['user_id']
        customer = Customer.objects.get(id=customer_id)

        if Like.objects.filter(user_id=customer_id, **validated_data).exists():
            raise serializers.ValidationError('You already liked this object')

        post_id = validated_data.get('post').id
        if not self.is_post_in_feed(customer, post_id):
            raise ValidationError('You cannot like this post')

        return Like.objects.create(user_id=customer_id, **validated_data)

    def is_post_in_feed(self, customer, post_id):
        following_ids = Follower.objects.filter(
            follower_user=customer).values_list('following_user_id', flat=True)

        return Post.objects.filter(
            Q(id=post_id) & (Q(author=customer) | Q(author_id__in=following_ids))
        ).exists()
