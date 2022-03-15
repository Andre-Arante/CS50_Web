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
    image = models.ImageField(upload_to='auctions\static', default='..auctions/static/default.jpg')

    def date_published():
        return self.date.strftime('%B %d %Y')

    def __str__(self):
        return f"{self.name} for ${self.selling_price}. Image can be found at {self.image}"
