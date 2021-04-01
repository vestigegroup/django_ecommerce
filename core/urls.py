from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('checkout', checkout, name='checkout'),
    path('products', products, name='products'),
]
