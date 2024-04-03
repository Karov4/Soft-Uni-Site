from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    USER_TYPE_CHOICES = (
        ('renter', 'Renter'),
        ('leaser', 'Leaser'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "age", "password1", "password2", "user_type")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'user_type')
