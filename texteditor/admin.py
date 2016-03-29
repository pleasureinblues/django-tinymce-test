from django.contrib import admin
from texteditor.models import Editor
# Register your models here.



class EditorAdmin (admin.ModelAdmin):
    list_display = ('title','content')

admin.site.register(Editor, EditorAdmin)