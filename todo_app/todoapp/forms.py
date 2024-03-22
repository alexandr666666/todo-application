from django import forms
from .models import Task

class FormTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['time', 'text']
        widgets = {
            'time': forms.TextInput(attrs={'placeholder': 'Введите дату'}),
            'text': forms.TextInput(attrs={'placeholder': 'Введите задачу'})
        }
        error_messages = {
            'text': {'required': ''},
            'time': {'required': ''}
        }

class FormSetting(forms.Form):
    OPTIONS = [
        ('light', 'Светлая тема'),
        ('dark', 'Темная тема')
    ]
    options = forms.ChoiceField(choices=OPTIONS, label='')

