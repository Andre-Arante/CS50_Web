from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    """
    Model that stores all neccesary data for a post
    """

    title = models.CharField(max_length=64)
    content = models.CharField(max_length=200)

    