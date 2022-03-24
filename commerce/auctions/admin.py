from django.contrib import admin

from .models import Auction_Listings, Category

# Register your models here.
admin.site.register(Auction_Listings)
# admin.site.register(Watchlist)
admin.site.register(Category)
# admin.site.register(Comment)
# admin.site.register(Bid)
