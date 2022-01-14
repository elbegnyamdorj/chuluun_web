from django.urls import path, include, re_path
from . import views
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    
    path(r'admin/', admin.site.urls),
    path(r'mn/', views.homeMN, name='mongolian'),
    path(r'en/', views.homeEN, name='english'),
    re_path(r'^.*$', RedirectView.as_view(url='mn/', permanent=False), name='index')
]
