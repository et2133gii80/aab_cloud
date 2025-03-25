from django.shortcuts import render
from django.views.generic import ListView

from files.models import Files


# Create your views here.

class FilesListView(ListView):
    model = Files
