from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# importing signals
from django.db.models.signals import post_save 
from django.dispatch import receiver

# USER manager
class CustomUserManager(BaseUserManager):
    '''
    this is user manager for managing user while registering By mobile and OTP
    '''
    
    def create_user(self, mobile, password, **extra_fields):
        '''
        create and save user with mobile and OTP 
        '''
        
        if not mobile:
            raise ValueError("mobile is required...!")
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
    
    def create_superuser(self, mobile, password=None, **other_fields):
        '''
        creating super user 
        '''
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser muse have is_superuser=True')
        return self.create_user(mobile, password, **other_fields)
    
    
    def create_user_with_pass(self, mobile, password, **other_fields):
        '''
        create and save user with mobile and password 
        '''
        if not mobile:
            raise ValueError("mobile is required...!")
        user = self.model(mobile=mobile, **other_fields)
        user.set_password(password)
        user.save()
        return user

# USER 
class Custom_User(AbstractBaseUser, PermissionsMixin):
    """
    generatin custom user for registering with OTP and EMAIL adress
    """
    name = models.CharField(max_length=50)
    
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=11, unique=True)
    
    is_superuser = models.BooleanField(default=True) # access to admin panel 
    is_staff = models.BooleanField(default=True)
    
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) 

    is_seller = models.BooleanField(default=False)
    
    otp = models.CharField(max_length=6, null=True, blank=True)  
    otp_expiry = models.DateTimeField(null=True, blank=True)  
    
    last_login = models.DateTimeField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'mobile'
    
    REQUIRED_FIELDS = [
        'name', "email"
    ]
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
  
class Buyer_Profile(models.Model):
    '''
    profile of user that add many infos to user model and save some infos 
    '''
    
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)

    # cart_history = models.ManyToManyField('cart.Cart', blank=True)
    buy_status = models.BooleanField(default=False)
    # buy_history = models.ManyToManyField('order.Order', blank=True)
    
    address_1 = models.TextField(null=True, blank=True)
    address_2 = models.TextField(null=True, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    meli_code = models.CharField(max_length=10, blank=True)
    
    # favorite_categories = models.ManyToManyField('products.Category', blank=True)
    product_points = models.PositiveIntegerField(default=0)
    # seen_products = models.ManyToManyField('products.Product', blank=True)

    def __str__(self):
        return self.first_name

    def get_last_orders(self):
        return self.buy_history.order_by('-created_at')[:5]
    
    def get_total_spent(self):
        return sum(order.total_price for order in self.buy_history.all())
    
    def add_to_wishlist(self, product):
        self.seen_products.add(product)
    
    def remove_from_wishlist(self, product):
        self.seen_products.remove(product)
        
''' signal for making buyer profile automaticly after creating user '''
@receiver(post_save, sender=Custom_User)
def save_buyer_profile(sender, instance, created, **kwargs):
    if created:
        Buyer_Profile.objects.create(user=instance)
        
        
class Seller_Profile(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    is_seller = True
    
    store_name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='seller_logos/', null=True, blank=True)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    zip_code = models.CharField(max_length=10, unique=True)
    meli_code = models.CharField(max_length=10, unique=True)
    
    # شناسه منحصر به فرد برای یک کسب و کار
    business_registration_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    # زمانی که فروشگاه فروشنده تاسیس شد
    established_date = models.DateField(null=True, blank=True)
    # موقعیت فیزیکی کسب و کار فروشنده
    location = models.CharField(max_length=255, null=True, blank=True)
    # ب سایت تجاری فروشنده
    website = models.URLField(max_length=200, null=True, blank=True)
    # JSON پیوندها به نمایه های رسانه های اجتماعی فروشنده به 
    social_media_links = models.JSONField(null=True, blank=True)
    # میانگین امتیاز فروشنده
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    # تعداد کل فروش های تکمیل شده
    number_of_sales = models.PositiveIntegerField(default=0)
    # روش ترجیحی فروشنده برای ارسال محصولات
    preferred_shipping_method = models.CharField(max_length=255, null=True, blank=True)
    # ایمیل اختصاصی برای پشتیبانی مشتری
    customer_support_email = models.EmailField(null=True, blank=True)
    # شماره تلفن برای پشتیبانی مشتری
    customer_support_phone = models.CharField(max_length=15, null=True, blank=True)
    # شماره حساب بانکی
    bank_account_number = models.CharField(max_length=20, null=True, blank=True)  
    # شماره_مسیر_بانک
    bank_routing_number = models.CharField(max_length=9, null=True, blank=True)
    

    def __str__(self):
        return self.store_name

    