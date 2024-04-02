from django.urls import path
from .views import ApartmentListView, ApartmentDetailView, LeaseCreateView, home, home_with_profile, add_apartment

urlpatterns = [
    path('', home, name='home'),
    path('home_with_profile/', home_with_profile, name='home_with_profile'),
    path('apartments/add/', add_apartment, name='add_apartment'),
    path('apartments/', ApartmentListView.as_view(), name='apartment_list'),
    path('apartments/<int:pk>/', ApartmentDetailView.as_view(), name='apartment_detail'),
    path('leases/new/', LeaseCreateView.as_view(), name='lease_create'),
]
