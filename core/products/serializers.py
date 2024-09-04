from rest_framework import serializers
from .models import Products, Category, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'user', 'rating', 'comment']

class ProductsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'about', 'image', 'seller', 'buyer_counts', 'status', 'category', 'created_date', 'updated_date', 'reviews']

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'children']
