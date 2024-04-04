from django import forms
from .models import Apartment, Rent


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'description', 'price', 'available', 'location', 'image_url']


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['start_date', 'end_date']