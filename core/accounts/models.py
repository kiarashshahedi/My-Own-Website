from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Custom_User(AbstractBaseUser):
    """
    generatin custom user for registering with OTP and EMAIL adress
    """
    name = models.CharField((""), max_length=50)
