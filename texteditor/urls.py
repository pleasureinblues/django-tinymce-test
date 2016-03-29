from django.conf.urls import patterns, url
from texteditor import views

urlpatterns = patterns('',
        url(r'^$', views.editor, name='editor'),
        url(r'^data-view/$', views.data_view, name='data_view'),
)