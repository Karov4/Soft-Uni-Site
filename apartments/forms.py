from django import forms
from django.core.exceptions import ValidationError

from .models import Apartment, Rent


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'description', 'price', 'available', 'location', 'image_url']


class EditApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'description', 'price', 'available', 'location', 'image_url']


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if end_date is not None and start_date is not None:
            if end_date < start_date:
                raise ValidationError("End date should not be earlier than start date.")