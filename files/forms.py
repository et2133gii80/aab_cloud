from django import forms
from .models import Files
from django.db import models
#from django.core.exceptions import ValidationError

class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('file_name','uploaded_file', )
        # labels = {'file_name':'',
        #           'uploaded_file': ''}
        widgets = {
            'uploaded_file': forms.FileInput(
                attrs={
                    'style': 'display: none'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(FilesForm, self).__init__(*args, **kwargs)
        self.fields['uploaded_file'].label = ""
        self.fields['file_name'].label = ""

        self.fields['file_name'].widget.attrs.update(
            {
                'class': 'file_name_form',
                'placeholder': 'filename'
            }
        )

        # self.fields['uploaded_file'].widget.attrs.update(
        #     {
        #         'class': 'upload_file_form',
        #         'placeholder': 'Drop files'
        #     }
        # )



