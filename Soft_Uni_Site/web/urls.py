from django.urls import path

from Soft_Uni_Site.web.views import index

urlpatterns = (
    path('', index, name='index'),
)