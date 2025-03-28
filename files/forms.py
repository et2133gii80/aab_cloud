from django import forms
from .models import Files
#from django.core.exceptions import ValidationError

class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('file_name', 'description','uploaded_file',)

    # def __init__(self, *args, **kwargs):
    #     super(FilesForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['uploaded_file'].widget.attrs.update(
    #         {
    #             'class': 'dropzone',
    #             'placeholder': 'Перетащите сюда файл'
    #         }
    #     )


