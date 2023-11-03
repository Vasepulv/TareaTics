from django.urls import path
from .views import *

urlpatterns = [
    path('shopping-cart', shopping_cart, name='shopping_cart'),
    path('payment', payment, name='payment')
]