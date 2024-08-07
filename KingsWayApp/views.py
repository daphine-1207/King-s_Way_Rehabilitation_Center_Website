from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *
from django.contrib import messages


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
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_data = form.cleaned_data
            Order.objects.create(
                full_name=order_data['full_name'],
                email=order_data['email'],
                phone_number=order_data['phone_number'],
                payment_option=order_data['payment_option'],  # Corrected key here

            )
            messages.success(request, 'Order made successfully!')
    else:
        form = OrderForm()
    return render(request, 'shop.html', {'form': form})



def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Subscription successful!'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'errors': 'Invalid request method'}, status=400)

@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Order submitted successfully!'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'errors': 'Invalid request method'}, status=400)
