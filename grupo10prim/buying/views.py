from django.shortcuts import render


# Create your views here.
def shopping_cart(request):
    return render(request, 'shopping-cart.html')


def payment(request):
    return render(request, 'payment.html')
