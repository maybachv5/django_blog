# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import comment_view,notifications,note_to_read,note_to_delete

urlpatterns = [
    url(r'^create/(?P<pk>\d+)/$',comment_view,name='comment_view'),
    url(r'^notifications/(?P<read>\w+)/$',notifications,name='notifications'),
    url(r'^notifications/(?P<read>\w+)/to_read/(?P<id>\d+)/$',note_to_read,name='note_to_read'),
    url(r'^notifications/(?P<read>\w+)/to_delete/(?P<id>\d+)/$',note_to_delete,name='note_to_delete'),
]