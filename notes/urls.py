from django.urls import path

from .views import RegisterView, success_view

app_name = "notes"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('success/', success_view, name='success')
]