import os.path

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import FileResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.exceptions import PermissionDenied
from config import settings
from files.forms import FilesForm, FoldersForm
from files.models import Files
from files.services import get_files_by_folders, get_favourites_files
from files.models import Folders


class FilesListView(ListView):
    model = Files
    #
    # def get_queryset(self):
    #     user_id = self.kwargs.get('pk')
    #     return get_files_by_folders(user_id=user_id)


class FilesCreateView(CreateView):
    model = Files
    form_class = FilesForm
    success_url = reverse_lazy('files:files_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # def get_form_class(self):
    #     files = self.get_object()
    #     if files.owner_id == self.request.user.id:
    #         return FilesForm


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

class FoldersCreateView(CreateView):
    model = Folders
    form_class = FoldersForm
    success_url = reverse_lazy('files:folders_list')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # def get_form_class(self):
    #     folders = self.get_object()
    #     if folders.owner_id == self.request.user.id:
    #         return FoldersForm

class FilesByFoldersView(ListView):
    model = Folders
    def get_queryset(self):
        folders_id = self.kwargs.get('pk')
        return get_files_by_folders(folders_id=folders_id)


class FavouritesFilesView(ListView):
    model = Files
    def get_queryset(self):
        return get_favourites_files()


# def download_file(request, file_name):
#     files_path = ''
#
#     if os.path.exists(files_path):
#         return FileResponse(open(files_path))

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