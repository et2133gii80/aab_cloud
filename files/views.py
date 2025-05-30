import os.path

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import FileResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from config import settings
from files.forms import FilesForm
from files.models import Files
from files.services import get_files_by_folders
from files.models import Folders


class FilesListView(ListView):
    model = Files

class FilesCreateView(CreateView):
    model = Files
    form_class = FilesForm
    success_url = reverse_lazy('files:files_list')

class FilesUpdateView(UpdateView):
    model = Files
    success_url = reverse_lazy('files:files_list')

class FilesDelete(DeleteView):
    model = Files
    success_url = reverse_lazy('files:files_list')
    permission_required = 'files:delete_file'

class FilesDetailView(DetailView):
    model = Files

class FoldersListView(ListView):
    model = Folders

class FilesByFoldersView(ListView):
    model = Folders
    def get_queryset(self):
        folders_id = self.kwargs.get('pk')
        return get_files_by_folders(folders_id=folders_id)


def download_file(request, file_name):
    files_path = ''

    if os.path.exists(files_path):
        return FileResponse(open(files_path))

# class FavouritesFilesListView(ListView):
#     model = Files
#
#     def get_queryset(self):


# def send_activate_email(request, user, token, form=None):
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     message = render_to_string('activate_mail.html', {
#         'user': user,
#         'domain': get_current_site(request).domain,
#         'uid': uid,
#         'token': token
#     })
#     to_email = form.cleaned_data.get('email')
#     send_mail(message, from_email=settings.EMAIL_HOST_USER, to=[to_email], fail_silently=False)