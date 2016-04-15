from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', 'tinymcetest.views.home', name='home'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^texteditor/', include('texteditor.urls', namespace='texteditor')),

    url(r'^admin/', include(admin.site.urls)),
]
