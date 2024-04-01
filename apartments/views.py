from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Apartment, Lease, Review


def home(request):
    return render(request, 'home.html')


class ApartmentListView(ListView):
    model = Apartment
    template_name = 'apartments/apartments_list.html'


class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'apartments/apartments_details.html'


class LeaseCreateView(CreateView):
    model = Lease
    fields = ['tenant', 'apartment', 'start_date', 'end_date']
    template_name = 'apartments/lease_form.html'


class ReviewCreateView(CreateView):
    model = Review
    fields = ['rating', 'comment', 'lease']
    template_name = 'apartments/review_form.html'