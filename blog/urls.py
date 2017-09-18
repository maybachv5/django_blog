# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import homeview,TimelineView


urlpatterns = [
    url(r'^$',homeview,name='home'),
    url(r'^timeline/$',TimelineView.as_view(),name='timeline'),

]