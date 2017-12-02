# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import wordsearch,wordsearch_api

urlpatterns = [
    url(r'^wordsearch/$',wordsearch,name='wordsearch'),
    url(r'^wordserach_api/$',wordsearch_api,name='wordsearch_api'),
]