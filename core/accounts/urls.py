from django.urls import path
from .views import RegisterAPIView, SignInAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
