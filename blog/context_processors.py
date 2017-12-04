# -*- coding: utf-8 -*-

from django.conf import settings
from datetime import datetime

# 自定义上下文管理器
def settings_info(request):
    return {
        'site_description':settings.SITE_DESCRIPTION,
        'site_keywords':settings.SITE_KEYWORDS,
        'blog_start_date':datetime(2017,9,1,0,0),
    }