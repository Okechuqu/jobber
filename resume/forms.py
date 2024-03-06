from django import forms
from .models import *


class UpdateResumeForm(forms.ModelForm):
    
    class Meta:
        model = Resume
        exclude = ("user",)
