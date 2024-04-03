from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView

from .forms import ApartmentForm
from .models import Apartment, Lease
from django.http import HttpResponseForbidden


def home(request):
    if request.user.is_authenticated:
        return redirect('home_with_profile')
    return render(request, 'home.html')


@login_required
def home_with_profile(request):
    apartments = Apartment.objects.all()
    return render(request, 'home_with_profile.html', {'apartments': apartments})


class LeaseCreateView(CreateView):
    model = Lease
    fields = ['tenant', 'apartment', 'start_date', 'end_date']
    template_name = 'apartments/lease_form.html'

    def form_valid(self, form):
        if self.request.user.groups.filter(name='Renters').exists():
            return HttpResponseForbidden("You are not allowed to perform this action.")
        return super().form_valid(form)


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


@login_required
def my_apartments(request):
    apartments = Apartment.objects.filter(owner=request.user)
    return render(request, 'apartments/my_apartments.html', {'apartments': apartments})


@login_required
def edit_apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id, owner=request.user)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('my_apartments')
    else:
        form = ApartmentForm(instance=apartment)
    return render(request, 'apartments/edit_apartment.html', {'form': form})

@login_required
def delete_apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id, owner=request.user)
    if request.method == 'POST':
        apartment.delete()
        return redirect('my_apartments')
    return render(request, 'apartments/confirm_delete.html', {'apartment': apartment})