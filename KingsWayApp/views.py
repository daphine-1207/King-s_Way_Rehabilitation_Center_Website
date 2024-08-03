from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from .models import Subscription

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

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Save the email to the database
            subscription, created = Subscription.objects.get_or_create(email=email)
            if created:
                return HttpResponse('Thank you for subscribing!')
            else:
                return HttpResponse('You are already subscribed!')
        else:
            return HttpResponse('Please enter a valid email address.')
    return redirect('/')