from django.contrib.auth import login
from django.views.generic import DetailView
from .models import UserProfile
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.models import Group


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'users/userprofile_detail.html'


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data.get('user_type')
            user_group = Group.objects.get(name=user_type.capitalize() + 's')  # Get the correct group
            user.groups.add(user_group)  # Add the user to the chosen group
            login(request, user)
            return redirect("login")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = NewUserForm
    return render(request=request, template_name="authentication/register.html", context={"register_form":form})



