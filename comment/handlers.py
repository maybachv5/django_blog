# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from .models import Comment,Notification

def notify_handler(sender,instance,**kwargs):
    the_article = instance.belong
    create_p = instance.author
    if instance.rep_to:
        '''如果评论是一个回复评论，则同时通知给文章作者和回复的评论人，如果2者相等，则只通知一次'''
        if the_article.author == instance.rep_to.author:
            get_p = instance.rep_to.author
            new_notify = Notification(create_p=create_p,get_p=get_p,to_article=the_article,to_comment=instance)
            new_notify.save()
        else:
            get_p1 = the_article.author
            get_p2 = instance.rep_to.author
            new1 = Notification(create_p=create_p,get_p=get_p1,to_article=the_article,to_comment=instance)
            new2 = Notification(create_p=create_p,get_p=get_p2,to_article=the_article,to_comment=instance)
            new1.save()
            new2.save()
    else:
        '''如果评论是一个一级评论而不是回复其他评论，则直接通知给文章作者'''
        get_p = the_article.author
        new_notify = Notification(create_p=create_p,get_p=get_p,to_article=the_article,to_comment=instance)
        new_notify.save()

post_save.connect(notify_handler,sender=Comment)
