from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('shop/', views.shop, name='shop'),
<<<<<<< HEAD
    path('thank-you/', views.thank_you, name='thank_you'),

=======
    path('subscribe/', views.subscribe, name='subscribe'),
>>>>>>> 7c108442faa956b61e0af085f577ae7e2f70f10c
]
