from django.urls import path
from .views import ApartmentListView, ApartmentDetailView, LeaseCreateView, home

urlpatterns = [
    path('', home, name='home'),
    path('apartments/', ApartmentListView.as_view(), name='apartment_list'),
    path('apartments/<int:pk>/', ApartmentDetailView.as_view(), name='apartment_detail'),
    path('leases/new/', LeaseCreateView.as_view(), name='lease_create'),
]
