from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'youtube.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^link/google/$', 'youtube.views.linkgoogle', name="linkgoogle"),
    url(r'^oauth2callback/$', 'youtube.views.callback', name='callback'),
    url(r'^channel/$', 'youtube.views.channel_id', name='channel_id'),
    url(r'^posted/$', 'youtube.views.info', name='info'),
)
