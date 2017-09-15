# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter
def get_email_secret(email):
    '''返回邮箱的省略形式'''
    e_right = email.split('@')[-1]
    e_left = email.split('@')[0]
    return e_left[:2]+'...'+'@'+e_right