from .views import PasswordNewView
from django.urls import path

urlpatterns = [
    path('password-reset', PasswordNewView.as_view(), name="password-reset"),
]