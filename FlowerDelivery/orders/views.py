from django.shortcuts import render

def cart(request):
    # Логика корзины (заглушка)
    return render(request, 'orders/cart.html', {})
