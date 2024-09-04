from rest_framework import serializers
from .models import Custom_User, Buyer_Profile, Seller_Profile, Address



class CustomUserSerializer(serializers.ModelSerializer):
    '''
        for custom_user model
    '''
    class Meta:
        model = Custom_User
        fields = ['id', 'name', 'email', 'mobile', 'is_superuser', 'is_staff', 'is_verified', 'is_active', 'is_seller', 'otp', 'otp_expiry', 'last_login', 'created_date', 'updated_date']

class BuyerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Buyer_Profile
        fields = ['user', 'first_name', 'last_name', 'date_of_birth', 'cart_history', 'buy_history', 'buy_status', 'meli_code', 'favorite_categories', 'product_points', 'seen_products']

class SellerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Seller_Profile
        fields = ['user', 'store_name', 'description', 'logo', 'first_name', 'last_name', 'profile_image', 'date_of_birth', 'zip_code', 'meli_code', 'mobile', 'business_registration_number', 'established_date', 'location', 'website', 'social_media_links', 'rating', 'number_of_sales', 'preferred_shipping_method', 'customer_support_email', 'customer_support_phone', 'bank_account_number', 'bank_routing_number']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['user', 'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country']