from django.urls import path
from .views import register_request, view_profile, edit_profile

urlpatterns = [
    path('register/', register_request, name='register'),
    path('profile/', view_profile, name='view_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
