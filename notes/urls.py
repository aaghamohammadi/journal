from django.urls import path

from .views import UserRegisterView, success_view, LandingPageView, ItemPageView

app_name = "notes"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("items/", LandingPageView.as_view(), name="landing-page"),
    path("items/<int:pk>/", ItemPageView.as_view(), name="item"),
    path("success/", success_view, name="success"),
]
