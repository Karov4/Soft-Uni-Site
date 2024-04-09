from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .forms import ApartmentForm, RentForm, EditApartmentForm, ReviewForm
from .models import Apartment, Rent, Review, Favorite
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse


def home(request):
    if request.user.is_authenticated:
        return redirect('home_with_profile')
    return render(request, 'home.html')


class HomeWithProfileView(LoginRequiredMixin, ListView):
    model = Apartment
    template_name = 'home_with_profile.html'
    context_object_name = 'apartments'


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
            return redirect('my_apartments')
    else:
        form = ApartmentForm()

    return render(request, 'apartments/apartment_add.html', {'form': form})


class MyApartmentsView(LoginRequiredMixin, ListView):
    model = Apartment
    template_name = 'apartments/my_apartments.html'
    context_object_name = 'apartments'

    def get_queryset(self):
        return Apartment.objects.filter(owner=self.request.user)


class MyRentsView(LoginRequiredMixin, ListView):
    model = Rent
    template_name = 'apartments/my_rents.html'
    context_object_name = 'rents'

    def get_queryset(self):
        return Rent.objects.filter(tenant_id=self.request.user)


@login_required
def edit_apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id, owner=request.user)
    if request.method == 'POST':
        form = EditApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('my_apartments')
    else:
        form = EditApartmentForm(instance=apartment)
    return render(request, 'apartments/edit_apartment.html', {'form': form})

@login_required
def delete_apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id, owner=request.user)
    if request.method == 'POST':
        apartment.delete()
        return redirect('my_apartments')
    return render(request, 'apartments/confirm_delete.html', {'apartment': apartment})


class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'apartments/apartment_details.html'


class FavoritesApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'apartments/apartment_details_from_favorites.html'


@login_required
def rent_apartment(request, apartment_id):
    """View to create a new rent for a specific apartment."""
    apartment = get_object_or_404(Apartment, pk=apartment_id)

    # Check if the apartment is available
    if not apartment.available:
        messages.error(request, 'This apartment is not available.')
        return HttpResponseRedirect(reverse('home_with_profile'))

    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            rent = form.save(commit=False)
            rent.tenant = request.user
            rent.apartment = apartment
            rent.save()
            # Update the apartment's availability
            apartment.available = False
            apartment.save()
            return HttpResponseRedirect(reverse('home_with_profile'))
    else:
        form = RentForm()
    return render(request, 'apartments/rent_apartment.html', {'form': form, 'apartment': apartment})


@login_required
def add_review(request, rent_id):
    rent = Rent.objects.get(id=rent_id)
    apartment = rent.apartment
    if not apartment.available:
        return HttpResponse("This apartment is not available for review.")

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.lease = rent
            review.save()
            return redirect('my_rents')
    else:
        form = ReviewForm()

    return render(request, 'apartments/add_review.html', {'form': form})


@login_required
def apartment_reviews(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    rents = apartment.rent_set.all()
    reviews = Review.objects.filter(lease__in=rents)

    return render(request, 'apartments/apartment_reviews.html', {'reviews': reviews})


@login_required
def add_favourite(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    # Check if the favourite already exists
    existing_favourite = Favorite.objects.filter(user=request.user, apartment=apartment)
    if existing_favourite.exists():
        return HttpResponse("This apartment is already in your favourites.")

    # If the favourite does not exist, create a new one
    favourite = Favorite(user=request.user, apartment=apartment)
    favourite.save()
    return redirect('home_with_profile')


@login_required
def user_favourites(request, user_id):
    favorites = Favorite.objects.filter(user__id=user_id)
    return render(request, 'apartments/user_favorites.html', {'favorites': favorites})


@login_required
def delete_favourite(request, apartment_id):
    # Get the apartment
    apartment = get_object_or_404(Apartment, id=apartment_id)

    # Check if the favourite exists
    favourite = Favorite.objects.filter(user=request.user, apartment=apartment)
    if favourite.exists():
        # If the favourite exists, delete it
        favourite.delete()
        return redirect(reverse('user_favourites', args=[request.user.id]))
    else:
        # If the favourite does not exist, inform the user
        return HttpResponse("This apartment is not in your favourites.")