from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import ApartmentForm
from .models import Apartment, Lease, Review
from django.http import HttpResponseForbidden


def home(request):
    if request.user.is_authenticated:
        return redirect('home_with_profile')
    return render(request, 'home.html')

@login_required
def home_with_profile(request):
    apartments = Apartment.objects.all()
    return render(request, 'home_with_profile.html', {'apartments': apartments})


class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'apartments/apartments_details.html'


class ReviewCreateView(CreateView):
    model = Review
    fields = ['rating', 'comment', 'lease']
    template_name = 'apartments/review_form.html'


class LeaseCreateView(CreateView):
    model = Lease
    fields = ['tenant', 'apartment', 'start_date', 'end_date']
    template_name = 'apartments/lease_form.html'

    def form_valid(self, form):
        if self.request.user.groups.filter(name='Renters').exists():
            return HttpResponseForbidden("You are not allowed to perform this action.")
        return super().form_valid(form)


class ApartmentListView(ListView):
    model = Apartment
    template_name = 'apartments/apartments_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Leasers').exists():
            return Apartment.objects.all()
        return Apartment.objects.filter(owner=self.request.user)


@login_required
def add_apartment(request):
    # Check if the user is in the 'Leasers' group
    if not request.user.groups.filter(name='Leasers').exists():
        return HttpResponseForbidden("You are not allowed to perform this action.")

    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.owner = request.user
            apartment.save()
            return redirect('apartment_detail', apartment.id)  # assuming you have a detail view for the Apartment model
    else:
        form = ApartmentForm()

    return render(request, 'apartments/apartment_add.html', {'form': form})
