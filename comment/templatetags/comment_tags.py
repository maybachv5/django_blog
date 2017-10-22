# -*- coding: utf-8 -*-
from django import template
from ..models import Comment


register = template.Library()

@register.simple_tag
def get_comment_list(article):
    '''获取评论列表'''
    comment_list = Comment.objects.filter(belong=article,parent=None)
    return comment_list

@register.simple_tag
def get_child_comments(parent_com):
    '''获取父评论的所有子评论列表'''
    childs = Comment.objects.filter(parent=parent_com)
    return childs

@register.simple_tag
def get_comment_author_count(article):
    lis = []
    for comment in article.comment_set.all():
        if comment.author not in lis:
            lis.append(comment.author)
    return len(lis)