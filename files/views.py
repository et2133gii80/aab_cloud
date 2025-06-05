from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView

from files.forms import FilesForm, FoldersForm
from files.models import Files, Folders
from files.services import (
    get_favourites_files,
    get_files_by_folders,
    recent_file_and_folders,
)


class FilesListView(LoginRequiredMixin,ListView):
    model = Files


class FilesCreateView(LoginRequiredMixin,CreateView):
    model = Files
    form_class = FilesForm
    success_url = reverse_lazy("files:files_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FilesDelete(LoginRequiredMixin,DeleteView):
    model = Files
    success_url = reverse_lazy("files:files_list")
    permission_required = "files:delete_file"


class FoldersListView(LoginRequiredMixin,ListView):
    model = Folders


class FoldersCreateView(LoginRequiredMixin,CreateView):
    model = Folders
    form_class = FoldersForm
    success_url = reverse_lazy("files:folders_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FoldersDelete(LoginRequiredMixin,DeleteView):
    model = Folders
    success_url = reverse_lazy("files:files_list")
    permission_required = "files:delete_folder"


class FilesByFoldersView(LoginRequiredMixin,ListView):
    model = Folders

    def get_queryset(self):
        folders_id = self.kwargs.get("pk")
        return get_files_by_folders(folders_id=folders_id)


class FavouritesFilesView(LoginRequiredMixin,ListView):
    model = Files

    def get_queryset(self):
        return get_favourites_files()


class RecentListView(LoginRequiredMixin,ListView):
    model = Folders, Files

    def get_queryset(self):
        return recent_file_and_folders()

