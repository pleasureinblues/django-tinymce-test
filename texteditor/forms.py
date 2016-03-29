from django import forms
from django.contrib.auth.models import User
from texteditor.models import Editor
from tinymce.widgets import TinyMCE


class EditorForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Name")
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 70, 'rows': 12}))

    class Meta:
        model = Editor
        fields = ('title', 'content')
