from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

DEFAULT_CATEGORY_ID = 1

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64, default="Misc")

    def __str__(self):
        return f"{self.name}"

class Auction_Listings(models.Model):
    """
    Model to control auction listings

    User can view listings via view_listings or active_listings
    edit via create_listings
    """

    ## Basic information
    name = models.CharField(max_length=64)
    selling_price = models.IntegerField(default=100)
    image = models.URLField(default='google.com')
    # description = models.TextField(default="Add description here.")
    creator = models.ForeignKey('User', related_name="person_who_created_item", on_delete=models.CASCADE)

    ## Listing page information
    closed = models.BooleanField(default=False)
    category = models.ForeignKey('Category', default=DEFAULT_CATEGORY_ID, on_delete=models.CASCADE, related_name="auction_category")

    ## Published timestamp
    def date_published(self):
        return self.date.strftime('%B %d %Y')
    
    def __str__(self):
        return f"{self.name}"

# ## Stores bid information
# class Bid(models.Model):
#     user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="bid_placer")
#     bid = models.IntegerField(default=100)
#     auction = models.ForeignKey("Auction_Listings", on_delete=models.CASCADE, related_name="auction_bidded_on")
    
#     ## Published timestamp
#     def date_published(self):
#         return self.date.strftime('%B %d %Y')

# ## Stores comment information
# class Comment(models.Model):
#     user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="comment_writer")
#     auction = models.ForeignKey("Auction_Listings", on_delete=models.CASCADE, related_name="auction_commented_on")
#     content = models.TextField(max_length=999)

#     ## Published timestamp
#     def date_published(self):
#         return self.date.strftime('%B %d %Y')

# ## Stores watchlist information
# class Watchlist(models.Model):
#     user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="watchlister")
#     auction = models.ForeignKey("Auction_Listings", on_delete=models.CASCADE, related_name="auction_watchlisted")

#     ## Published timestamp
#     def date_published(self):
#         return self.date.strftime('%B %d %Y')