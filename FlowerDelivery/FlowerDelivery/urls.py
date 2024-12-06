from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),
    path('', home, name='home'),
]

