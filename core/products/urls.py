from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, CategoryViewSet, ReviewViewSet


router = DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
