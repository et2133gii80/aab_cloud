from django.urls import path

from files import views

app_name = 'files'

urlpatterns = [
    path('',views.FilesListView.as_view(), name='files_list'),
    path('folders/',views.FoldersListView.as_view(), name='folders_list'),
    path('files/<int:pk>/', views.FilesDetailView.as_view(), name='files_detail'),
    path('files/create/', views.FilesCreateView.as_view(), name='files_create'),
    path('files/update/<int:pk>/', views.FilesUpdateView.as_view(), name='files_update'),
    path('files/delete/<int:pk>/', views.FilesDelete.as_view(), name='files_delete'),
    path('folders/<int:pk>/', views.FilesByFoldersView.as_view(), name= 'files_by_folders'),
    # path('activate/<uidb64>/<token>', views.send_activate_email, name='activate')
]