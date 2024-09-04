from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Custom_User, Buyer_Profile, Seller_Profile, Address
from .serializers import CustomUserSerializer, BuyerProfileSerializer, SellerProfileSerializer, AddressSerializer
from django.contrib.auth import authenticate, login
from datetime import timezone


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = Custom_User.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        mobile = request.data.get('mobile')
        password = request.data.get('password')
        user = Custom_User.objects.create_user(mobile=mobile, password=password)
        user.generate_otp()
        # Send OTP using Kavenegar service
        return Response({'message': 'User registered successfully, OTP sent to mobile.'})

    @action(detail=False, methods=['post'])
    def login(self, request):
        mobile = request.data.get('mobile')
        otp = request.data.get('otp')
        user = Custom_User.objects.get(mobile=mobile)
        if user.verify_otp(otp):
            user.last_login = timezone.now()
            user.save()
            # Implement token generation for login
            return Response({'message': 'Login successful'})
        return Response({'error': 'Invalid OTP'}, status=400)

class BuyerProfileViewSet(viewsets.ModelViewSet):
    queryset = Buyer_Profile.objects.all()
    serializer_class = BuyerProfileSerializer

class SellerProfileViewSet(viewsets.ModelViewSet):
    queryset = Seller_Profile.objects.all()
    serializer_class = SellerProfileSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
