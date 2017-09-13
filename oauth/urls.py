# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import profile_view


urlpatterns = [
    url(r'^profile/$',profile_view,name='oauth_profile'),

]