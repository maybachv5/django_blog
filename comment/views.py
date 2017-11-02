from django.shortcuts import render

from blog.models import Article
from .models import Comment
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

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
