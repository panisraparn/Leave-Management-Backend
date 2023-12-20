from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "user_id",
            "password1",
            "password2",
            "fname",
            "lname",
            "role"
        )
