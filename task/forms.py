from django import forms 
from django.forms import ModelForm

from .models import *


class TASKForm(forms.ModelForm):
    title  = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add new task......'}))

    class Meta:
        model = TASK
        fields  = '__all__'



