from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^search', views.search, name='search'),
    url(r'^admin/', include(admin.site.urls)),
)
