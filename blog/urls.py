# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import IndexView,TimelineView,DetailView,CategoryView,TagView,MySearchView,Aboutview


urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^timeline/$',TimelineView.as_view(),name='timeline'),
    url(r'^article/(?P<article_id>\d+)/$',DetailView.as_view(),name='detail'),
    url(r'^category/(?P<slug>[a-zA-Z0-9_\-\u4e00-\u9fa5]+)/$',CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<slug>[a-zA-Z0-9_\-\u4e00-\u9fa5]+)/$',TagView.as_view(),name='tag'),
    url(r'^search/?$', MySearchView.as_view(), name='search_view'),
    url(r'^about/$',Aboutview,name='about'),
]