from rest_framework import serializers
from .models import Custom_User, Buyer_Profile, Seller_Profile


class CustomUserSerializer(serializers.ModelSerializer):
    '''
    for custom_user model
    '''
    class Meta:
        model = Custom_User
        fields = ['id', 'name', 'email', 'mobile', 'is_seller', 'is_active', 'is_verified']

class BuyerProfileSerializer(serializers.ModelSerializer):
    '''
    for buyer_profile model
    '''
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Buyer_Profile
        fields = '__all__'
        read_only_fields = ('user',)

class SellerProfileSerializer(serializers.ModelSerializer):
    '''
    for seller_profile model
    '''
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Seller_Profile
        fields = '__all__'
        read_only_fields = ('user',)
