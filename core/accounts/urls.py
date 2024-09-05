from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomUserViewSet, BuyerProfileViewSet, SellerProfileViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'buyer-profiles', BuyerProfileViewSet)
router.register(r'seller-profiles', SellerProfileViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

    
