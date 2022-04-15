# Generated by Django 4.0.3 on 2022-04-13 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_remove_friendship_creator_remove_friendship_friend_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default='Hidden', on_delete=django.db.models.deletion.CASCADE, related_name='user_who_posted', to=settings.AUTH_USER_MODEL),
        ),
    ]