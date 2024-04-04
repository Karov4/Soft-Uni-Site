from django.urls import path
from .views import register_request, ProfileView, edit_profile

urlpatterns = [
    path('register/', register_request, name='register'),
    path('profile/', ProfileView.as_view(), name='view_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
