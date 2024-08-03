from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
<<<<<<< HEAD
from .forms import DonationForm
=======
from .models import Subscription
>>>>>>> 7c108442faa956b61e0af085f577ae7e2f70f10c

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

# def donate(request):
#     return render(request, 'donate.html')

def shop(request):
    return render(request, 'shop.html')

<<<<<<< HEAD

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def thank_you(request):
    return render(request, 'donations/thank_you.html')
=======
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
>>>>>>> 7c108442faa956b61e0af085f577ae7e2f70f10c
