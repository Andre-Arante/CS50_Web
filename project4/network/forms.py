from django import forms

class Create_Post(forms.Form):
    content = forms.CharField(max_length=200, required=False, widget=forms.Textarea)