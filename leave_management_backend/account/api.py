from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .forms import SignupForm
from django.contrib.auth.forms import PasswordChangeForm


@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "username": request.user.username,
            "user_id": request.user.user_id,
            "role": request.user.role,
            "fname": request.user.fname,
            "lname": request.user.lname,
            "email": request.user.email,
            "username": request.user.username,
            "prefix": request.user.prefix,
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
            "prefix": data.get("prefix"),
        }
    )

    if form.is_valid():
        print("save na")
        form.save()
        # send vertification email later!
    else:
        print("Signup fail: form error")
        print(form.errors)
        message = "error"
    return JsonResponse({"message": message})


@api_view(["POST"])
def editpassword(request):
    user = request.user

    form = PasswordChangeForm(data=request.POST, user=user)

    if form.is_valid():
        form.save()

        return JsonResponse({"message": "success"})
    else:
        return JsonResponse({"message": form.errors.as_json()}, safe=False)
