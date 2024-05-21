from django.db import models
from django.conf import settings


class Person(models.Model):
    MEMBERSHIP_REGULAR = 'R'
    MEMBERSHIP_PRIME = 'P'

    MEMBERSHIP_CHOICES = [(MEMBERSHIP_REGULAR, 'Regular'),
                          (MEMBERSHIP_PRIME, 'Prime')]

    phone = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)
    membership_status = models.CharField(
        max_length=1, default=MEMBERSHIP_REGULAR, choices=MEMBERSHIP_CHOICES)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    follower_user = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='followers')
    following_user = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='followings')
    created_at = models.DateTimeField(auto_now_add=True)
