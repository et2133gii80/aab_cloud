from django.contrib.gis.geos import io
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from files.forms import FilesForm
from files.models import Files


# Create your views here.

class FilesListView(ListView):
    model = Files


class FileCreateView(CreateView):
    model = Files
    template_name = 'files/files_form.html'
    success_url = reverse_lazy('files:files_list')
    form_class = FilesForm

