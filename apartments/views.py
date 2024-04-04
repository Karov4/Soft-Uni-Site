from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, ListView

from .forms import ApartmentForm
from .models import Apartment, Lease
from django.http import HttpResponseForbidden


def home(request):
    if request.user.is_authenticated:
        return redirect('home_with_profile')
    return render(request, 'home.html')


class HomeWithProfileView(LoginRequiredMixin, ListView):
    model = Apartment
    template_name = 'home_with_profile.html'
    context_object_name = 'apartments'


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


class MyApartmentsView(LoginRequiredMixin, ListView):
    model = Apartment
    template_name = 'apartments/my_apartments.html'
    context_object_name = 'apartments'

    def get_queryset(self):
        return Apartment.objects.filter(owner=self.request.user)


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