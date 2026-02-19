from django.urls import path
from . import admin, views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
]