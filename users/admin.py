from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'age', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(CustomUser, CustomUserAdmin)
