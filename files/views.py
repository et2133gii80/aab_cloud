from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


class FileDetailView(DetailView):
    model = Files


# class FileUpdateView(UpdateView):
#     model = Files
#     success_url = reverse_lazy('files:files_list')


# class FileDeleteView(PermissionRequiredMixin, DeleteView):
#     model = Files
#     template_name = 'files/files_confirm_delete.html'
#     success_url = reverse_lazy('files:files_list')
#     permission_required = 'files.delete_file'



