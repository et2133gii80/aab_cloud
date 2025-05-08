from lib2to3.fixes.fix_input import context

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from files.forms import FilesForm
from files.models import Files, Folders


# Create your views here.


# def list_view(request):
#     folders = Folders.objects.all()
#     files = Files.objects.select_related('folders')
#     return render(request, 'list_view.html', {
#         'folders': folders,
#         'files': files
#     })

class FilesListView(ListView):
    model = Files

    def get_context_data(self, **kwargs):
        context = super(FilesListView, self).get_context_data(**kwargs)
        return context

class FilesCreateView(CreateView):
    model = Files
    form_class = FilesForm
    success_url = reverse_lazy('files:files_list')

#
#
# class FileCreateView(CreateView):
#     model = Files
#     template_name = 'files/files_form.html'
#     success_url = reverse_lazy('files:files_list')
#     form_class = FilesForm
#
#
# class FileDetailView(DetailView):
#     model = Files



# class FileUpdateView(UpdateView):
#     model = Files
#     success_url = reverse_lazy('files:files_list')


# class FileDeleteView(PermissionRequiredMixin, DeleteView):
#     model = Files
#     template_name = 'files/files_confirm_delete.html'
#     success_url = reverse_lazy('files:files_list')
#     permission_required = 'files.delete_file'



