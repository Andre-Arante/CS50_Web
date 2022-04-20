from logging import PlaceHolder
from socket import fromshare
from django import forms

from .models import Post, UserProfile

class CreatePost(forms.ModelForm):
    def __init__(self, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreatePost, self).__init__(**kwargs)
        self.fields['content'].required = False

    def save(self, commit=True):
        obj = super(CreatePost, self).save(commit=False)
        obj.user = self.user
        if commit:
            obj.save()
        return obj

    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': "What's going on...",
        'style': 'font-size: xx-large',
        'autocomplete': 'off',
        }), initial='')
    class Meta:
        model = Post
        fields = ['content']
