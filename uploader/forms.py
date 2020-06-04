from django import forms


class UploadForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='选择文件...',
        help_text='最大100M'
    )