from django import forms

from .models import Files, Folders


class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ["file_name", "uploaded_file", "folder", "favorite"]

    def __init__(self, *args, **kwargs):
        super(FilesForm, self).__init__(*args, **kwargs)

        self.fields["file_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название товара"}
        )

        self.fields["uploaded_file"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание товара"}
        )

        self.fields["folder"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Загрузите изображение"}
        )

        self.fields["favorite"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберете категорию"}
        )


class FoldersForm(forms.ModelForm):
    class Meta:
        model = Folders
        fields = ["folders_name"]
        # widgets = {
        #     'file_name': forms.TextInput(attrs={
        #         'class': 'file_name_form',
        #         'placeholder': 'filename'
        #     }),
        #     'uploaded_file': forms.FileInput(attrs={
        #         'class': 'uploaded_file_form',
        #         # 'style': 'display: none;'
        #     })
        # }
        labels = {
            "folders_name": "",
        }
        help_texts = {
            "folders_name": "",
        }

        # labels = {'file_name':'',
        #           'uploaded_file': ''}

    def __init__(self, *args, **kwargs):
        super(FoldersForm, self).__init__(*args, **kwargs)

        self.fields["folders_name"].widget.attrs.update(
            {
                # 'class': 'file_name_form',
                "placeholder": "folders_name"
            }
        )
