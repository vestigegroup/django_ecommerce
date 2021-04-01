from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


def index(request):
    context = {
        'items': Item.objects.all(),
    }
    return render(request, 'home.html', context)


def checkout(request):
    return render(request, 'checkout-page.html')


def products(request):
    return render(request, 'product-page.html')
