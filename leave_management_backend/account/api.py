from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .forms import SignupForm


@api_view(["GET"])
def me(request):
    return JsonResponse(
        {"id": request.user.id,
         "username": request.user.username,
         "user_id": request.user.user_id,
         "fname": request.user.fname,
         "lname": request.user.lname,
         "email": request.user.email,
         "username": request.user.username
         }
    )


# signup
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = "success"

    form = SignupForm(
        {
            "username": data.get("username"),
            "email": data.get("email"),
            "user_id": data.get("user_id"),
            "fname": data.get("fname"),
            "lname": data.get("lname"),
            "role": data.get("role"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    if form.is_valid():
        print("save na")
        form.save()
        # send vertification email later!
    else:
        print("signup failed")
        print("form error")
        print(form.errors)
        message = "error"
    return JsonResponse({"message": message})
