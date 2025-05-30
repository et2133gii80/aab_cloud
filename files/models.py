from sys import maxsize

from django.db import models
class Folders(models.Model):
    folders_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.folders_name}'

    class Meta:
        verbose_name = 'папка'
        verbose_name_plural = 'папки'



class Files(models.Model):
    file_name = models.CharField(max_length=150)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    uploaded_file = models.FileField(upload_to='files/users_files', verbose_name='загрузка файла',)
    favorite = models.BooleanField(default=False)
    folder = models.ForeignKey(Folders, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f'{self.file_name}'


    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'



