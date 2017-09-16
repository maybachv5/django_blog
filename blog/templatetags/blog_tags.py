# -*- coding: utf-8 -*-
# 修改了自定义标签要重启服务器

from django import template

register = template.Library()

@register.filter
def get_email_secret(email):
    '''返回邮箱的省略形式'''
    e_right = email.split('@')[-1]
    e_left = email.split('@')[0]
    return e_left[:2]+'...'+'@'+e_right

@register.filter
def get_show_name(user):
    '''返回用户的展示名，优先选择昵称'''
    if user.nickname:
        return user.nickname
    return user.username

@register.inclusion_tag('blog/tags/user-avatar.html')
def get_show_avatar(user):
    '''返回一个用户的展示头像<img>标签，优先用网络头像'''
    return {'user':user}
