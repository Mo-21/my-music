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

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    follower_user = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='followers')
    following_user = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='followings')
    created_at = models.DateTimeField(auto_now_add=True)
