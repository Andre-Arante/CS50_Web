from django import forms

choices = (
    ("Home and Decor", "Home and Decor"),
    ("Entertainment", "Entertainment"),
    ("Work and Office", "Work and Office")
)
class Create_Form(forms.Form):
    name = forms.CharField(label="Enter item name here", max_length=64)
    selling_price = forms.IntegerField(label="Enter item price here: ")
    image = forms.URLField()
    category = forms.ChoiceField(choices=choices, label="Enter category name here")

class Edit_Form(forms.Form):
    closed = forms.BooleanField()

class Bid_Form(forms.Form):
    watchlisted = forms.BooleanField(label="Placing a bid requires adding the item to your watchlist. Check box to continue.")
    bid = forms.IntegerField()

class Category_Form(forms.Form):
    category = forms.ChoiceField(choices=choices, label="Enter category name here")