from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home_logged_in.html')
    else:
        return render(request, 'home_not_logged_in.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'login_and_register_templates/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            pass
    return render(request, 'login_and_register_templates/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')