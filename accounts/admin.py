from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

custom_user = get_user_model()


class CustomUserAdmin(UserAdmin):
    """
    Configures admin panel views for CustomUsers.
    https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#modeladmin-options
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = custom_user
    # Which fields will be listed in admin section (on the list, not 'details' page):
    list_display = [
        "email",
        "username",
        "is_superuser",
        "address",
    ]
    # Which fields to show when editing user via admin panel:
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("address",)}), )
    # Which fields to show when creating user via admin panel:
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("address",)}), )


admin.site.register(custom_user, CustomUserAdmin)
