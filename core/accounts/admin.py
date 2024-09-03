from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Custom_User, Buyer_Profile, Seller_Profile

class CustomUserAdmin(BaseUserAdmin):
    model = Custom_User
    list_display = ['email', 'mobile', 'name', 'is_active', 'is_superuser', 'is_verified']
    search_fields = ['mobile']
    list_filter = ('is_seller',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'mobile')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_verified', 'is_seller')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'mobile', 'password1', 'password2', 'is_active', 'is_superuser', 'is_verified', 'is_seller'),
        }),
    )

    ordering = ('email',)  # or 'mobile' if you prefer

# Register the custom user model with the admin site
admin.site.register(Custom_User, CustomUserAdmin)

# register Buyer profile in admin page
admin.site.register(Buyer_Profile)