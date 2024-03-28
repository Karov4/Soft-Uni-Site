from django import forms
from .models import RentalApplication

class RentalApplicationForm(forms.ModelForm):
    class Meta:
        model = RentalApplication
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your message here...'}),
        }