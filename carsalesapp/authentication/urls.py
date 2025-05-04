from . import views
from django.urls import path
from .views import CustomPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView


urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/change_password_done.html'
    ), name='change_password_done'),
]