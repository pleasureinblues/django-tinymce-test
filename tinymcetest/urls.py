from django.conf.urls import include, url
from django.contrib import admin
from texteditor import views

urlpatterns = [
    # Examples:
    url(r'^$', views.editor, name='editor'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^texteditor/', include('texteditor.urls', namespace='texteditor')),

    url(r'^admin/', include(admin.site.urls)),
]
