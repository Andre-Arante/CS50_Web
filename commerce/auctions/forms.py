from django import forms

default_categories = ("Household", "Outdoors", "Work-Related", "Pets", "Used", "New", "Games")

class Create_Form(forms.Form):
    name = forms.CharField(label="Enter item name here", max_length=64)
    selling_price = forms.IntegerField(label="Enter item price here: ")
    image = forms.URLField()
    category = forms.CharField(label="Enter category name here", max_length=64)

class Edit_Form(forms.Form):
    closed = forms.BooleanField()

class Bid_Form(forms.Form):
    watchlisted = forms.BooleanField(label="Placing a bid requires adding the item to your watchlist. Check box to continue.")
    bid = forms.IntegerField()