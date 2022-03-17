from django import forms

class Create_Form(forms.Form):
    name = forms.CharField(label="Enter item name here: ", max_length=64)
    selling_price = forms.IntegerField(label="Enter item price here: ")
    image = forms.URLField()