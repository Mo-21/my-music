# Generated by Django 5.0.6 on 2024-05-30 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_artist_name_alter_genre_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='playlistitem',
            unique_together={('playlist', 'song')},
        ),
    ]