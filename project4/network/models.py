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

    def get_followers(self):
        user = self.user
        return Friendship.objects.filter(following=user)

    def __str__(self):
        return self.user.username

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = (('post', 'user'),)

    def __str__(self):
        return f"{self.post} : {self.user}"