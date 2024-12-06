from django.db import models
from users.models import User
from catalog.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return sum(product.price for product in self.products.all())

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
