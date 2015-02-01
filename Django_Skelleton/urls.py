from django.conf.urls import patterns, include, url
from django.contrib import admin
from Django_Skelleton import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_Skelleton.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
