
from django import forms
from .models import Job


class IbiomesForm(forms.ModelForm):
    class Meta:
        model=Job
        fields =('userid',)
