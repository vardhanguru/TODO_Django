from django import forms
from django.forms import ModelForm
from .models import *

class TaskForms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description']
        exclude=['created','complete']

