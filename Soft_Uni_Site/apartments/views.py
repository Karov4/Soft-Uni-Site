from django.shortcuts import render

from Soft_Uni_Site.apartments.models import Apartment


def apartment_list(request):
    apartments = Apartment.objects.filter(available=True)
    return render(request, 'apartments/list.html', {'apartments': apartments})
