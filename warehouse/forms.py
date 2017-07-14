from django import forms
from django.forms import ModelForm
from .models import Upload

class UploadFileForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['fil']

class AddDomainForm(forms.Form):
    domain = forms.CharField(strip=True)
