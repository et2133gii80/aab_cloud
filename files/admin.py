from django.contrib import admin
from .models import Files
@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name')
    search_fields = ('file_name', 'description')


from django.contrib import admin
from .models import Folders
@admin.register(Folders)
class FoldersAdmin(admin.ModelAdmin):
    list_display = ('id', 'folders_name')
    search_fields = ('folders_name',)



