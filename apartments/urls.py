from django.urls import path
from .views import home, HomeWithProfileView, add_apartment, MyApartmentsView, edit_apartment, delete_apartment

urlpatterns = [
    path('', home, name='home'),
    path('home_with_profile/', HomeWithProfileView.as_view(), name='home_with_profile'),
    path('apartments/add/', add_apartment, name='add_apartment'),
    path('my_apartments/', MyApartmentsView.as_view(), name='my_apartments'),
    path('edit_apartment/<int:apartment_id>/', edit_apartment, name='edit_apartment'),
    path('delete_apartment/<int:apartment_id>/', delete_apartment, name='delete_apartment'),
]
