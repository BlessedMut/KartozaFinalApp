from django import forms
from django.contrib import admin
from easy_maps.widgets import AddressWithMapWidget

from .models import Profiles


class UserForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('username', 'first_name', 'email', 'password', 'address')

        widgets = {
            'address': AddressWithMapWidget({'class': 'vTextField'})
        }

