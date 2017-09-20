# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import IndexView,TimelineView,DetailView


urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^timeline/$',TimelineView.as_view(),name='timeline'),
    url(r'^article/(?P<article_id>\d+)/$',DetailView.as_view(),name='detail'),

]