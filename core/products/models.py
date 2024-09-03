from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Seller_Profile

User = get_user_model()

class Products(models.Model):
    '''
    this is a class to define products for products app 
    '''
    name = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField()
    seller = models.ForeignKey(Seller_Profile, on_delete=models.CASCADE)
    buyer_counts = models.IntegerField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class category(models.Model):
    """
    this is category for ordering products of products app
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    children = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
