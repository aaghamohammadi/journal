from django.urls import path

from .views import (
    UserRegisterView,
    success_view,
    LandingPageView,
    ItemPageView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
)

app_name = "notes"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("items/", LandingPageView.as_view(), name="landing-page"),
    path("create/", ItemCreateView.as_view(), name="create"),
    path("items/<int:pk>/", ItemPageView.as_view(), name="item"),
    path("item-edit/<int:pk>/", ItemUpdateView.as_view(), name="edit"),
    path("item-delete/<int:pk>/", ItemDeleteView.as_view(), name="delete"),
    path("success/", success_view, name="success"),
]
