from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from products.models import Products

def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')
