"""message_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^message_list/', MessageListView.as_view()), 
    url(r'^comments/(?P<pk>[0-9]+)/$', 'main.views.comments'),
    url(r'^message_create/', 'main.views.message_create'),
    url(r'^comment_create/(?P<pk>[0-9]+)/$', 'main.views.comment_create'), 
 	url(r'^delete_comment/(?P<pk>[0-9]+)/$', 'main.views.delete_comment'), 
 	url(r'^delete_message/(?P<pk>[0-9]+)/$', 'main.views.delete_message'), 


]
