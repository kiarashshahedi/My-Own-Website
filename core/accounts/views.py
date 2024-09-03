from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import BuyerRegistrationForm, SellerRegistrationForm
from .models import Custom_User
# api
import random
from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .models import Custom_User, Buyer_Profile, Seller_Profile
from .serializers import CustomUserSerializer, BuyerProfileSerializer, SellerProfileSerializer


# normal part 

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

# API part

class RegisterBuyerView(APIView):
    '''
    register buyer_profile
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        mobile = request.data.get('mobile')
        name = request.data.get('name')

        if not mobile or not name :
            return Response({'error': 'Mobile, name, and email are required'}, status=status.HTTP_400_BAD_REQUEST)

        if Custom_User.objects.filter(mobile=mobile).exists():
            return Response({'error': 'Mobile number already registered'}, status=status.HTTP_400_BAD_REQUEST)

        otp = random.randint(100000, 999999)
        user = Custom_User.objects.create_user(mobile=mobile, password=None, name=name, otp=str(otp))
        user.is_active = False  # Inactive until OTP is verified
        user.save()

        # Send OTP via SMS (Implement SMS sending here)
        print(f"Send OTP {otp} to mobile {mobile}")  # Placeholder for actual SMS sending

        return Response({'message': 'OTP sent to mobile', 'user_id': user.id}, status=status.HTTP_201_CREATED)


class VerifyOTPView(APIView):
    '''
    CHEKING OTP 
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data.get('user_id')
        otp = request.data.get('otp')

        if not user_id or not otp:
            return Response({'error': 'User ID and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Custom_User.objects.get(id=user_id)
        except Custom_User.DoesNotExist:
            return Response({'error': 'Invalid User ID'}, status=status.HTTP_400_BAD_REQUEST)

        if user.otp == otp and user.otp_expiry > timezone.now():
            user.is_active = True
            user.is_verified = True
            user.otp = None
            user.otp_expiry = None
            user.save()

            # Create or fetch Token for authenticated user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'OTP verified successfully', 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterSellerView(APIView):
    '''
    REGISTER SELLER_PROFILE 
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        mobile = request.data.get('mobile')
        meli_code = request.data.get('meli_code')
        store_name = request.data.get('store_name')
        email = request.data.get('email')

        if not mobile or not meli_code or not store_name or not email:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        if Custom_User.objects.filter(mobile=mobile).exists() or Seller_Profile.objects.filter(meli_code=meli_code).exists():
            return Response({'error': 'Mobile number or Meli code already registered'}, status=status.HTTP_400_BAD_REQUEST)

        otp = random.randint(100000, 999999)
        user = Custom_User.objects.create_user(mobile=mobile, password=None, email=email, otp=str(otp))
        user.is_active = False  # Inactive until OTP is verified
        user.is_seller = True
        user.save()

        Seller_Profile.objects.create(user=user, meli_code=meli_code, store_name=store_name)

        # Send OTP via SMS (Implement SMS sending here)
        print(f"Send OTP {otp} to mobile {mobile}")  # Placeholder for actual SMS sending

        return Response({'message': 'OTP sent to mobile', 'user_id': user.id}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """
    LOGIN 
    """
    permission_classes = [AllowAny]

    def post(self, request):
        mobile = request.data.get('mobile')
        password = request.data.get('password')

        if not mobile or not password:
            return Response({'error': 'Mobile and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(mobile=mobile, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
