from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from orders.models import Order  # Для отображения истории заказов

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Перенаправление на личный кабинет
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'users/dashboard.html', {'orders': orders})
