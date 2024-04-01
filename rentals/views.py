# views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import Apartment, Landlord, Tenant
from .forms import LeaseForm, UserRegistrationForm


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class ApartmentListView(View):
    def get(self, request):
        apartments = Apartment.objects.all()
        return render(request, 'apartments/apartments_list.html', {'apartments': apartments})


@login_required
def dashboard(request):
    try:
        request.user.landlord
        return redirect('landlord_dashboard')
    except Landlord.DoesNotExist:
        pass

    try:
        request.user.tenant
        return redirect('tenant_dashboard')
    except Tenant.DoesNotExist:
        pass

    return redirect('home')


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'authentication/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data.get('user_type') == 'landlord':
                Landlord.objects.create(user=user)
            else:
                Tenant.objects.create(user=user)
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'authentication/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'authentication/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if hasattr(user, 'landlord'):
                return redirect('landlord_dashboard')
            elif hasattr(user, 'tenant'):
                return redirect('tenant_dashboard')
            else:
                return redirect('home')  # or wherever you want to redirect users who are neither landlords nor tenants
        else:
            return render(request, 'authentication/login.html', {'form': form})

class LandlordDashboardView(View):
    @login_required
    def get(self, request):
        apartments = Apartment.objects.filter(landlord__user=request.user)
        return render(request, 'landlord_dashboard.html', {'apartments': apartments})

class TenantDashboardView(View):
    @login_required
    def get(self, request):
        apartments = Apartment.objects.exclude(landlord__user=request.user)
        return render(request, 'tenant_dashboard.html', {'apartments': apartments})