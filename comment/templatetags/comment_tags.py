# -*- coding: utf-8 -*-
from django import template
from ..models import Comment,Notification


register = template.Library()


@register.simple_tag
def get_coms_count(article):
    '''获取评论总数'''
    comment_list = Comment.objects.filter(belong=article)
    return comment_list.count()

@register.simple_tag
def get_comment_list(article):
    '''获取父评论列表'''
    comment_list = Comment.objects.filter(belong=article,parent=None)
    return comment_list

@register.simple_tag
def get_child_comments(parent_com):
    '''获取父评论的所有子评论列表'''
    childs = Comment.objects.filter(parent=parent_com)
    return childs

@register.simple_tag
def get_comment_author_count(article):
    '''获取参与评论人数'''
    lis = []
    for comment in article.comment_set.all():
        if comment.author not in lis:
            lis.append(comment.author)
    return len(lis)

@register.simple_tag
def get_notifications(user,read):
    '''返回一个人的提示消息列表'''
    if read == 'read':
        return Notification.objects.filter(get_p=user,is_read=False)
    else:
        return Notification.objects.filter(get_p=user)

@register.simple_tag
def get_note_count(user,read):
    '''返回一个信息提示总数'''
    if read == 'read':
        notes = Notification.objects.filter(get_p=user,is_read=False)
    else:
        notes = Notification.objects.filter(get_p=user)
    return notes.count()

