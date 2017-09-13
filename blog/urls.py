# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import homeview


urlpatterns = [
    url(r'^$',homeview,name='home'),

]