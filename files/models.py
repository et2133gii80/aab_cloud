from django.db import models

# Create your models here.


class Files(models.Model):
    file_name = models.CharField(max_length=150, verbose_name='имя файла')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    #owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.file_name}'

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'
