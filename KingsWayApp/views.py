from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def donate(request):
    return render(request, 'donate.html')

def shop(request):
    return render(request, 'shop.html')
