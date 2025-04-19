from tkinter.constants import CASCADE

from django.db import models
# Create your models here.


class Folders(models.Model):
    folder_name = models.CharField(max_length=30, verbose_name='имя папки')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')



    def __str__(self):
        return f'{self.folder_name}'

    class Meta:
        verbose_name = 'папка'
        verbose_name_plural = 'папки'



class Files(models.Model):
    file_name = models.CharField(max_length=150, verbose_name='имя файла')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    #owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='files/users_files', verbose_name='загрузка файла')
    folder_name = models.ForeignKey(Folders,  on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return f'{self.file_name}'

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'



