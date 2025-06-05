from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegisterView, email_verification

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
]
