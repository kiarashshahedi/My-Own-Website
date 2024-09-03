from django.db import models
from products.models import Products
from accounts.models import Custom_User, Buyer_Profile

class CartItem(models.Model):
    user = models.ForeignKey(Buyer_Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.product.name} ({self.quantity})'
