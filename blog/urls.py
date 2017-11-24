# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import IndexView,TimelineView,DetailView,CategoryView,TagView,MySearchView,Aboutview



urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^timeline/$',TimelineView.as_view(),name='timeline'),
    url(r'^article/(?P<slug>[\w-]+)/$',DetailView.as_view(),name='detail'),
    url(r'^category/(?P<slug>[\w-]+)/$',CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<slug>[\w-]+)/$',TagView.as_view(),name='tag'),
    url(r'^search/?$', MySearchView.as_view(), name='search_view'),
    url(r'^about/$',Aboutview,name='about'),
]