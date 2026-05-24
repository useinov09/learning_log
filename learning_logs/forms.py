from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

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
