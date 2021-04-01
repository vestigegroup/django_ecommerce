from django.shortcuts import render
from .models import Item


def index(request):
    return render(request, 'home-page.html')


def checkout(request):
    return render(request, 'checkout-page.html')


def products(request):
    return render(request, 'product-page.html')
