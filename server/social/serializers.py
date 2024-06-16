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
    authored_posts = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'profile_image',
                  'phone', 'birthdate', 'membership_status',
                  'liked_posts', 'authored_posts']

    def get_authored_posts(self, obj):
        posts = getattr(obj, 'authored_posts', None)
        if posts is None:
            return []
        return PostSerializer(posts, many=True).data


class PostAuthorSerializer(serializers.ModelSerializer):
    user = LocalUserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user', 'profile_image', 'membership_status']


class CommentSerializer(serializers.ModelSerializer):
    user = CustomerSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    author = PostAuthorSerializer(read_only=True)
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

    def update(self, instance, validated_data):
        if instance.author.id != self.context['author_id']:
            raise serializers.ValidationError('You cannot update this post')
        return super().update(instance, validated_data)


class FollowerSerializer(serializers.ModelSerializer):
    follower_user = CustomerSerializer(read_only=True)
    following_user = CustomerSerializer(read_only=True)

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
        read_only_fields = ['post', 'created_at', 'user']

    def create(self, validated_data):
        customer_id = self.context['user_id']
        customer = Customer.objects.get(id=customer_id)
        post_id = self.context['post_id']

        like = Like.objects.filter(
            user_id=customer_id, post_id=post_id, **validated_data)
        if like.exists():
            return like.delete()

        if not self.is_post_in_feed(customer, post_id):
            raise ValidationError('You cannot like this post')

        return Like.objects.create(user_id=customer_id, post_id=post_id, **validated_data)

    def is_post_in_feed(self, customer, post_id):
        following_ids = Follower.objects.filter(
            follower_user=customer).values_list('following_user_id', flat=True)

        return Post.objects.filter(
            Q(id=post_id) & (Q(author=customer) | Q(author_id__in=following_ids))
        ).exists()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text', 'created_at']
        read_only_fields = ['post', 'created_at', 'user']

    def create(self, validated_data):
        customer_id = self.context['user_id']
        customer = Customer.objects.get(id=customer_id)

        post_id = self.context['post_id']
        if not self.is_post_in_feed(customer, post_id):
            raise ValidationError('You cannot comment on this post')

        return Comment.objects.create(user_id=customer_id, post_id=post_id, ** validated_data)

    def update(self, instance, validated_data):
        if instance.user_id != self.context['user_id']:
            raise serializers.ValidationError('You cannot update this comment')
        return super().update(instance, validated_data)

    def is_post_in_feed(self, customer, post_id):
        following_ids = Follower.objects.filter(
            follower_user=customer).values_list('following_user_id', flat=True)

        return Post.objects.filter(
            Q(id=post_id) & (Q(author=customer) | Q(author_id__in=following_ids))
        ).exists()
