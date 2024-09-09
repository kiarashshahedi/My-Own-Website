from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Custom_User
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view

# Register User (Signup)
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        mobile = data.get('mobile')
        password = data.get('password')
        name = data.get('name')
        email = data.get('email')

        if Custom_User.objects.filter(mobile=mobile).exists():
            return Response({"error": "User with this mobile already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if Custom_User.objects.filter(email=email).exists():
            return Response({"error": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = Custom_User.objects.create_user_with_pass(mobile=mobile, password=password, name=name, email=email)
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "user": CustomUserSerializer(user).data}, status=status.HTTP_201_CREATED)


# Sign-in User
class SignInAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        password = request.data.get('password')

        user = authenticate(mobile=mobile, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": CustomUserSerializer(user).data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid mobile or password"}, status=status.HTTP_400_BAD_REQUEST)


# Logout User
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
