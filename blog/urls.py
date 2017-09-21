# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import IndexView,TimelineView,DetailView,CategoryView,TagView,MySearchView


urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^timeline/$',TimelineView.as_view(),name='timeline'),
    url(r'^article/(?P<article_id>\d+)/$',DetailView.as_view(),name='detail'),
    url(r'^category/(?P<pk>\d+)/$',CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>\d+)/$',TagView.as_view(),name='tag'),
    url(r'^search/?$', MySearchView.as_view(), name='search_view'),  # 自己重写的URL

]