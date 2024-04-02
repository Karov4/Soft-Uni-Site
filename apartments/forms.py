from django import forms
from .models import Apartment


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'description', 'price', 'available', 'location', 'image_url']
