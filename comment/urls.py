# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import comment_view

urlpatterns = [
    url(r'^create/(?P<pk>\d+)/$',comment_view,name='comment_view'),
]