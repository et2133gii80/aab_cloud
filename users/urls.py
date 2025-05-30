from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView,custom_logout



app_name = 'users'

urlpatterns =[path('register/', RegisterView.as_view(), name='register'),
              path('login/', LoginView.as_view(template_name = 'users/login.html'), name = 'login' ),
              path('logout/', custom_logout, name = 'logout')]