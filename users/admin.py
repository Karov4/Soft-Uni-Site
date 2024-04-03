from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'age')
    list_filter = ('user_type',)
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)