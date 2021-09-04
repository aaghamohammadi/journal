from django.urls import path

from .views import UserRegisterView, success_view, UserLoginView

app_name = "notes"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("success/", success_view, name="success"),
]
