from django.urls import path
from . import views

urlpatterns = [
    
    # Normal Views :
    path('buyer/register/', views.buyer_register, name='buyer_register'),
    path('seller/register/', views.seller_register, name='seller_register'),
    
    # API Views :
    path('register/buyer/', views.RegisterBuyerView.as_view(), name='register-buyer'),
    path('verify-otp/', views.VerifyOTPView.as_view(), name='verify-otp'),
    path('register/seller/', views.RegisterSellerView.as_view(), name='register-seller'),
    path('login/', views.LoginView.as_view(), name='login'),
    
]