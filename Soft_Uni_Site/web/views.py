from django.forms import forms
from django.shortcuts import render


def index(request):
    return render(request, 'home_no_profile.html')
