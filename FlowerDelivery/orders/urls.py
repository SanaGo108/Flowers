from django.urls import path
from . import views

urlpatterns = [
    # Пример маршрута для корзины (замените на ваши представления)
    path('cart/', views.cart, name='cart'),
]
