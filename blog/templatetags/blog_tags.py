# -*- coding: utf-8 -*-
# 修改了自定义标签要重启服务器

from django import template
from ..models import Article, Category, Tag, Timeline, Carousel
from django.db.models.aggregates import Count
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag
def get_carousel_list():
    '''获取轮播图片列表'''
    return Carousel.objects.all()



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
    lis = Tag.objects.all()
    return [each for each in lis if each.get_article_list().count() > 0]


@register.simple_tag
def get_category_list():
    '''返回文章分类列表'''
    lis = Category.objects.all()
    return [each for each in lis if each.get_article_list().count() > 0]


@register.simple_tag
def get_star(num):
    '''得到一排星星'''
    tag_i = '<i class="glyphicon glyphicon-star"></i>'
    return mark_safe(tag_i * num)


@register.simple_tag
def get_star_title(num):
    '''得到星星个数的说明'''
    the_dict = {
        1: '1颗星：微更新，涉及轻微调整或者后期规划了内容',
        2: '2颗星：小更新，小幅度调整，一般不会迁移表格',
        3: '3颗星：中等更新，一般会增加或减少模块，有表格的迁移',
        4: '4颗星：大更新，涉及到应用的增减',
        5: '5颗星：最大程度更新，一般涉及多个应用和表格的变动',
    }
    return the_dict[num]


@register.inclusion_tag('blog/tags/user-avatar.html')
def get_show_avatar(user):
    '''返回一个用户的展示头像<img>标签，优先用网络头像'''
    return {'user': user}

@register.inclusion_tag('blog/tags/article-summary.html')
def load_article_summary(article):
    '''返回文章列表模板'''
    return {'article':article}

@register.inclusion_tag('blog/tags/paging.html',takes_context=True)
def load_pages(context):
    '''分页标签模板，不需要传递参数，直接继承参数'''
    return context

@register.simple_tag
def my_highlight(text,q):
    '''自定义标题搜索词高亮函数'''
    try:
        r = text.replace(q,'<span class="highlighted">{}</span>'.format(q))
        return mark_safe(r)
    except:
        return text
