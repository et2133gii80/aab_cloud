from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DeleteView, ListView

from files.forms import FilesForm, FoldersForm
from files.models import Files, Folders
from files.services import (get_favourites_files, get_files_by_folders,
                            recent_file_and_folders)


# @method_decorator(cache_page(60*15), name='dispatch')
class FilesListView(ListView):
    model = Files


class FilesCreateView(CreateView):
    model = Files
    form_class = FilesForm
    success_url = reverse_lazy("files:files_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FilesDelete(DeleteView):
    model = Files
    success_url = reverse_lazy("files:files_list")
    permission_required = "files:delete_file"


# @method_decorator(cache_page(60*15), name='dispatch')
class FoldersListView(ListView):
    model = Folders


class FoldersCreateView(CreateView):
    model = Folders
    form_class = FoldersForm
    success_url = reverse_lazy("files:folders_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FoldersDelete(DeleteView):
    model = Folders
    success_url = reverse_lazy("files:files_list")
    permission_required = "files:delete_folder"


# @method_decorator(cache_page(60*15), name='dispatch')
class FilesByFoldersView(ListView):
    model = Folders

    def get_queryset(self):
        folders_id = self.kwargs.get("pk")
        return get_files_by_folders(folders_id=folders_id)


# @method_decorator(cache_page(60*15), name='dispatch')
class FavouritesFilesView(ListView):
    model = Files

    def get_queryset(self):
        return get_favourites_files()


# @method_decorator(cache_page(60*15), name='dispatch')
class RecentListView(ListView):
    model = Folders, Files

    def get_queryset(self):
        return recent_file_and_folders()


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
