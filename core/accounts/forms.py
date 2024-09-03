# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Custom_User, Buyer_Profile, Seller_Profile

class BuyerRegistrationForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = ['mobile', 'name', 'email']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = False  # Ensure this user is a buyer
        if commit:
            user.save()
        return user

class SellerRegistrationForm(UserCreationForm):
    meli_code = forms.CharField(max_length=10, required=True)
    mobile = forms.CharField(max_length=11, required=True)

    class Meta:
        model = Custom_User
        fields = ['name', 'email', 'meli_code', 'mobile']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True  # Ensure this user is a seller
        if commit:
            user.save()
            Seller_Profile.objects.create(user=user, meli_code=self.cleaned_data['meli_code'], mobile=self.cleaned_data['mobile'])
        return user
