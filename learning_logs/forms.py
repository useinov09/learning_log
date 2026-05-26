from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={
            'rows': 5,  # высота textarea в строках
            'class': 'form-control',  # Bootstrap стиль — рамка, скругление
            'placeholder': 'Enter your topic here...',  # подсказка внутри поля
        })}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={
            'rows': 5,                  # высота textarea в строках
            'class': 'form-control',    # Bootstrap стиль — рамка, скругление
            'placeholder': 'Enter your notes here...',  # подсказка внутри поля
        })}

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].max_length = 15
        self.fields['username'].widget.attrs['maxlength'] = 15
        self.fields['username'].help_text = 'Maximum of 15 characters'
