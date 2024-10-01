from django import forms
from .models import Custom_User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['name', 'email', 'mobile', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
