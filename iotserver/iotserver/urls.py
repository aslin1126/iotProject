from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iotserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^$', 'iotserver.views.home'),
    url(r'^record/$', 'iotserver.views.listrecords'),
    url(r'^saverecord/(.+)$', 'iotserver.views.saverecord'),
)

