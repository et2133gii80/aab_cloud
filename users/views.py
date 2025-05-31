from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.core.cache import cache
from django.shortcuts import redirect

from .models import User


class RegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')


def custom_logout(request):
    cache.delete('files_list')
    logout(request)
    return redirect('/')