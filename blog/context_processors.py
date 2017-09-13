# -*- coding: utf-8 -*-

from django.conf import settings

# 自定义上下文管理器
def settings_info(request):
    return {
        'site_description':settings.SITE_DESCRIPTION,
        'site_keywords':settings.SITE_KEYWORDS,
    }