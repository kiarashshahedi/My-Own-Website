from django.urls import path
from . import views

urlpatterns = [
    path('buyer/register/', views.buyer_register, name='buyer_register'),
    path('seller/register/', views.seller_register, name='seller_register'),
]