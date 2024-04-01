from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Landlord, Tenant, Apartment, Lease, Payment


class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['landlord', 'address', 'rent']  # add additional fields here

class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = ['tenant', 'apartment', 'start_date', 'end_date']  # add additional fields here

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['lease', 'date', 'amount']  # add additional fields here