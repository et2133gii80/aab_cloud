from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [ path('', views.FilesListView.as_view(), name='files_list'),
                path('files/create/', views.FileCreateView.as_view(), name= 'files_create'),
                path('file/<int:pk>', views.FileDetailView.as_view(), name= 'files_detail')


]