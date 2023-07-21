from django import forms
from store.models import Posts
from django.forms import ModelForm


class CartAddProductForm(ModelForm):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    class Meta:
        model = Posts
        fields = ['update',]