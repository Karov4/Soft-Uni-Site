
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from users.views import register_request

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', include('users.urls')),  # assuming registration view is in users app
    path('', include('apartments.urls')),  # assuming home view is in apartments app
]
