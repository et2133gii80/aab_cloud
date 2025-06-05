from django.urls import path
from django.views.decorators.cache import cache_page
from files import views

app_name = "files"

urlpatterns = [
    path("", cache_page(60)(views.FilesListView.as_view()), name="files_list"),
    path(
        "folders/", cache_page(60)(views.FoldersListView.as_view()), name="folders_list"
    ),
    path("files/create/", views.FilesCreateView.as_view(), name="files_create"),
    path("files/delete/<int:pk>/", views.FilesDelete.as_view(), name="files_delete"),
    path(
        "folders/delete/<int:pk>/", views.FoldersDelete.as_view(), name="folders_delete"
    ),
    path(
        "folders/<int:pk>/",
        cache_page(60)(views.FilesByFoldersView.as_view()),
        name="files_by_folders",
    ),
    path("folders/create/", views.FoldersCreateView.as_view(), name="folders_create"),
    path(
        "files/",
        cache_page(60)(views.FavouritesFilesView.as_view()),
        name="files_by_favourites",
    ),
    path(
        "files/recent",
        cache_page(60)(views.RecentListView.as_view()),
        name="recent_files_and_folders",
    ),
]
