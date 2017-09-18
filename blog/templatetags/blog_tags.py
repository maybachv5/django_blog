# -*- coding: utf-8 -*-
# 修改了自定义标签要重启服务器

from django import template
from ..models import Article, Category, Tag, Timeline
from django.db.models.aggregates import Count
from django.utils.html import mark_safe

register = template.Library()


@register.filter
def get_email_secret(email):
    '''返回邮箱的省略形式'''
    e_right = email.split('@')[-1]
    e_left = email.split('@')[0]
    return e_left[:2] + '...' + '@' + e_right


@register.filter
def get_show_name(user):
    '''返回用户的展示名，优先选择昵称'''
    if user.nickname:
        return user.nickname
    return user.username

@register.simple_tag
def get_tag_list():
    '''返回标签列表,不能使用annotate方法，因为这种方法不能过滤掉草稿文章'''
    # return Tag.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)
    tag_list = []
    lis = Tag.objects.all()
    for each in lis:
        if each.get_article_list().count() > 0:
            tag_list.append(each)
    return tag_list


@register.simple_tag
def get_category_list():
    '''返回文章分类列表'''
    cate_list = []
    for each in Category.objects.all():
        if each.get_article_list().count() > 0:
            cate_list.append(each)
    return cate_list

@register.simple_tag
def get_star(num):
    '''得到一排星星'''
    tag_i = '<i class="glyphicon glyphicon-star"></i>'
    return mark_safe(tag_i*num)

@register.inclusion_tag('blog/tags/user-avatar.html')
def get_show_avatar(user):
    '''返回一个用户的展示头像<img>标签，优先用网络头像'''
    return {'user': user}
