from django.shortcuts import render,redirect

from blog.models import Article
from .models import Comment,Notification
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from . import handlers
from datetime import datetime
from django.shortcuts import get_object_or_404

user_model = settings.AUTH_USER_MODEL

@require_POST
def comment_view(request,pk):
    if request.is_ajax():
        data = request.POST
        new_user = request.user
        new_content = data['content']
        article_id = data['belong']
        the_article = Article.objects.get(id=article_id)
        parent_id = data['parent_id']
        rep_id = data['rep_id']
        if parent_id == 'base':
            new_comment = Comment(author=new_user,content=new_content,belong=the_article,parent=None,rep_to=None)
        else:
            new_parent = Comment.objects.get(id=parent_id)
            new_rep_id = rep_id.replace('rep-','')
            new_rep_to = Comment.objects.get(id=new_rep_id)
            new_comment = Comment(author=new_user, content=new_content, belong=the_article, parent=new_parent, rep_to=new_rep_to)
        new_comment.save()
        new_point = '#rep-' + str(new_comment.id)
        return JsonResponse({'msg':'评论提交成功！','new_point':new_point})
    return JsonResponse({'msg': '评论失败！'})

@login_required
def notifications(request,read):
    '''展示提示消息列表'''
    user = request.user
    now_date = datetime.now()
    return render(request,'comment/notification.html',context={'user':user,'read':read,'now_date':now_date})

@login_required
def note_to_read(request,read,id):
    '''将一个消息标记为已读'''
    user = request.user
    note = get_object_or_404(Notification,get_p=user,id=id)
    note.is_read = True
    note.save()
    now_date = datetime.now()
    return render(request, 'comment/notification.html', context={'user': user, 'read': read, 'now_date': now_date})

@login_required
def note_to_delete(request,read,id):
    '''将一个消息标记为已读'''
    user = request.user
    note = get_object_or_404(Notification,get_p=user,id=id)
    note.delete()
    now_date = datetime.now()
    return render(request, 'comment/notification.html', context={'user': user, 'read': read, 'now_date': now_date})




