from django.urls import path
from . import views
from .views import RegisterView, dashboard, LandlordDashboardView, TenantDashboardView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('apartments/', views.ApartmentListView.as_view(), name='apartment_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('landlord_dashboard/', LandlordDashboardView.as_view(), name='landlord_dashboard'),
    path('tenant_dashboard/', TenantDashboardView.as_view(), name='tenant_dashboard'),
    #path('payment/new/', views.PaymentCreateView.as_view(), name='payment_new'),
    #path('tenant/<int:pk>/', views.TenantDetailView.as_view(), name='tenant_detail'),
    #path('landlord/<int:pk>/', views.LandlordDetailView.as_view(), name='landlord_detail'),
    #path('apartment/<int:pk>/', views.ApartmentDetailView.as_view(), name='apartment_detail'),
    #path('lease/<int:pk>/', views.LeaseDetailView.as_view(), name='lease_detail'),
    #path('payment/<int:pk>/', views.PaymentDetailView.as_view(), name='payment_detail'),
]
