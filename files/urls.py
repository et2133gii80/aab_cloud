from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [ path('', views.FilesListView.as_view(), name='files_list'),

]