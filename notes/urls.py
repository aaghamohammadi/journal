from django.urls import path

from .views import UserRegisterView, success_view

app_name = "notes"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("success/", success_view, name="success"),
]
