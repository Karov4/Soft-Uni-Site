from django.urls import path
from .views import (home, HomeWithProfileView, add_apartment, MyApartmentsView, edit_apartment, delete_apartment,
                    rent_apartment, ApartmentDetailView, MyRentsView, add_review, apartment_reviews, add_favourite,
                    UserFavoritesView, delete_favourite, FavoritesApartmentDetailView)


urlpatterns = [
    path('', home, name='home'),
    path('home_with_profile/', HomeWithProfileView.as_view(), name='home_with_profile'),
    path('apartments/add/', add_apartment, name='add_apartment'),
    path('my_apartments/', MyApartmentsView.as_view(), name='my_apartments'),
    path('edit_apartment/<int:apartment_id>/', edit_apartment, name='edit_apartment'),
    path('delete_apartment/<int:apartment_id>/', delete_apartment, name='delete_apartment'),
    path('home_with_profile/apartment/<int:pk>/', ApartmentDetailView.as_view(), name='apartment_detail'),
    path('rent/<int:apartment_id>/', rent_apartment, name='rent_apartment'),
    path('my_rents/', MyRentsView.as_view(), name='my_rents'),
    path('add_review/<int:rent_id>/', add_review, name='add_review'),
    path('apartment/<int:apartment_id>/reviews/', apartment_reviews, name='apartment_reviews'),
    path('apartment/<int:apartment_id>/add_favourite/', add_favourite, name='add_favourite'),
    path('user/<int:user_id>/favourites/', UserFavoritesView.as_view(), name='user_favourites'),
    path('favorites/apartment/<int:pk>/', FavoritesApartmentDetailView.as_view(), name='apartment_detail_from_favorites'),
    path('delete_favourite/<int:apartment_id>/', delete_favourite, name='delete_favourite'),
]
