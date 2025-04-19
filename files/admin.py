from django.contrib import admin
from .models import Files, Folders

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name')
    search_fields = ('file_name', 'description')

@admin.register(Folders)
class FoldersAdmin(admin.ModelAdmin):
    list_display = ('id', 'folder_name')
    search_fields = ('folder_name', 'description')




