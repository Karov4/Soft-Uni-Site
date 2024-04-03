from django.contrib import admin
from .models import Apartment, Lease, Review, Favorite


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available', 'owner', 'location')
    list_filter = ('available', 'owner')
    search_fields = ('name', 'description', 'location')
    ordering = ('price',)


class LeaseAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'apartment', 'start_date', 'end_date')
    list_filter = ('tenant', 'apartment')
    search_fields = ('tenant__username', 'apartment__name')
    ordering = ('start_date',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'lease', 'date')
    list_filter = ('rating', 'lease')
    search_fields = ('comment',)
    ordering = ('date',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'user')
    list_filter = ('apartment', 'user')
    search_fields = ('apartment__name', 'user__username')
    ordering = ('user',)


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Lease, LeaseAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)
