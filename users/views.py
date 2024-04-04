from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView
from .models import CustomUser
from django.shortcuts import render, redirect
from .forms import NewUserForm, CustomUserChangeForm
from django.contrib.auth.models import Group


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data.get('user_type')

            # Create the group if it doesn't exist
            group_name = user_type.capitalize() + 's'
            group, created = Group.objects.get_or_create(name=group_name)

            user.groups.add(group)  # Add the user to the chosen group
            login(request, user)
            return redirect("login")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = NewUserForm
    return render(request=request, template_name="authentication/register.html", context={"register_form": form})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/view_profile.html'


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})