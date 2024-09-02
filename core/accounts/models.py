from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# USER manager
class UserManager(BaseUserManager):
    '''
    this is user manager for managing user while registering By mobile and OTP
    '''
    
    def create_user(self, mobile, email, password, **extra_fields):
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
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser muse have is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser muse have is_superuser=True')
        return self.create_user(mobile, password, **other_fields)
    
    
    def create_user_with_pass(self, mobile, password, username, **other_fields):
        '''
        create and save user with mobile and password 
        '''
        if not mobile:
            raise ValueError("mobile is required...!")
        user = self.model(mobile=mobile, username=username **other_fields)
        user.set_password(password)
        user.save()
        return user




# USER 
class Custom_User(AbstractBaseUser, PermissionError):
    """
    generatin custom user for registering with OTP and EMAIL adress
    """
    name = models.CharField((""), max_length=50)
    
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.IntegerField(max_length=11, unique=True)
    
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) # access to admin panel 
    is_verified = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    
    otp = models.CharField(max_length=6, null=True, blank=True)  
    otp_expiry = models.DateTimeField(null=True, blank=True)  
    
    last_login = models.DateTimeField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'mobile'
    
    REQUIRED_FIELDS = [
        'name', 'email', 'mobile'
    ]
    
    objects = UserManager()
    
    def __init__(self):
        return self.mobile