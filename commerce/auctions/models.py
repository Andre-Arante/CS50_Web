from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Auction_Listings(models.Model):
    """
    Model to control auction listings

    User can view listings via view_listings or active_listings
    edit via create_listings
    """

    name = models.CharField(max_length=64)
    selling_price = models.IntegerField(default=100)
    image = models.URLField(default='google.com')

    def date_published(self):
        return self.date.strftime('%B %d %Y')
