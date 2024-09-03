from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import BuyerRegistrationForm, SellerRegistrationForm
from .models import Custom_User

def buyer_register(request):
    '''
    registering buyers 
    '''
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('buyer_dashboard')  # Redirect to buyer dashboard after registration
    else:
        form = BuyerRegistrationForm()
    return render(request, 'accounts/buyer_register.html', {'form': form})

def seller_register(request):
    '''
    registering sellers
    '''
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('seller_dashboard')  # Redirect to seller dashboard after registration
    else:
        form = SellerRegistrationForm()
    return render(request, 'accounts/seller_register.html', {'form': form})
