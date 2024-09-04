from django.db import models
from products.models import Products
from accounts.models import Custom_User, Buyer_Profile

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(Buyer_Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# CartItem Model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(default=1)
    cart_quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.product.name} ({self.quantity})'
