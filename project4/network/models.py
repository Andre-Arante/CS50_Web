from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

import datetime

class User(AbstractUser):
    pass


class Post(models.Model):
    """
    Model that stores all neccesary data for a post
    """

    content = models.CharField(max_length=400)
    user = models.ForeignKey('User', related_name="user_who_posted", on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.content

class Friendship(models.Model):
    root = models.ForeignKey(User, related_name="friendship_creator", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="friend_set", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.root} is following {self.following}"

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    description = models.CharField(max_length=400, default="I am an arbitrary user with zero personality...")

    def get_following(self):
        user = self.user
        return Friendship.objects.filter(root=user)

    def __str__(self):
        return self.user.username

# class Comment(models.Model):
#     commentor = models.ForeignKey(User, related_name="commentor", on_delete=models.CASCADE)
#     content = models.CharField(max_length=200)
#     post = models.ForeignKey('Post', related_name="comment_location", on_delete=models.CASCADE)
