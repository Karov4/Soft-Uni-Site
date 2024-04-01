from django.urls import path
from .views import UserProfileDetailView, register_request

urlpatterns = [
    path('users/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile_detail'),
    path('register/', register_request, name='register'),
]
