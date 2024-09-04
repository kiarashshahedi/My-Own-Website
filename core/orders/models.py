from django.db import models
from accounts.models import Buyer_Profile
from products.models import Products
from payments.models import Payment



# Order Model
class Order(models.Model):
    user = models.ForeignKey(Buyer_Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    
# OrderItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_payment(self):
        from payments.models import Payment  # Import inside the method to avoid circular import
        return Payment.objects.filter(order=self)
