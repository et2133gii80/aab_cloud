from django.urls import path

from files import views

app_name = 'files'

urlpatterns = [ path('', views.FilesListView.as_view(), name='files_list'),
                path('folders/', views.FoldersListView.as_view(), name='folders_list')

                # path('files/create/', views.FileCreateView.as_view(), name= 'files_create'),
                # path('files/<int:pk>', views.FileDetailView.as_view(), name= 'files_detail'),

                # path('file/update/<int:pk>', views.FileUpdateView.as_view(), name= 'files_update')
                # path('files/delete/<int:pk>', views.FileDeleteView.as_view(), name= 'files_delete')
]