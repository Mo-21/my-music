# Generated by Django 5.0.6 on 2024-05-21 22:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_follower_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Customer',
        ),
    ]
