from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # The password field is implicitly included, no need to explicitly include it
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        # The password field is implicitly included, no need to explicitly include it
        fields = (
            "email",
            "username",
            "address",
        )
