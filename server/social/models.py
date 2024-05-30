from django.db import models
from django.conf import settings
from django.contrib import admin


class Customer(models.Model):
    MEMBERSHIP_REGULAR = 'R'
    MEMBERSHIP_PRIME = 'P'

    MEMBERSHIP_CHOICES = [(MEMBERSHIP_REGULAR, 'Regular'),
                          (MEMBERSHIP_PRIME, 'Prime')]

    phone = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)
    membership_status = models.CharField(
        max_length=1, default=MEMBERSHIP_REGULAR, choices=MEMBERSHIP_CHOICES)
    profile_image = models.ImageField(
        upload_to='social/images', default='social/images/default.png')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='social/posts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    follower_user = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='followers')
    following_user = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='followings')
    created_at = models.DateTimeField(auto_now_add=True)
