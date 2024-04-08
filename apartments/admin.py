from django.contrib import admin
from .models import Apartment, Rent, Review, Favorite


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'location')
    list_filter = ('available',)
    search_fields = ('name', 'location')
    ordering = ('name',)
    readonly_fields = ('owner',)


class RentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'apartment', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('tenant__username', 'apartment__name')
    ordering = ('-start_date',)
    readonly_fields = ('tenant', 'apartment')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('lease', 'rating', 'date')
    list_filter = ('rating', 'date')
    search_fields = ('lease__tenant__username', 'lease__apartment__name')
    ordering = ('-date',)
    readonly_fields = ('lease',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'apartment')
    list_filter = ('user',)
    search_fields = ('user__username', 'apartment__name')
    ordering = ('user',)
    readonly_fields = ('user', 'apartment')


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Rent, RentAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)
