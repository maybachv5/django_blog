from django.shortcuts import render

from .models import Article,Tag,Category,Timeline
from django.views import generic
# Create your views here.
import markdown
from markdown.extensions.toc import TocExtension   # 锚点的拓展
from django.utils.text import slugify              # 这个目测是URL支持中文的拓展


class IndexView(generic.ListView):
    # 指定视图
    template_name = 'blog/index.html'
    # 重命名返回的列表
    context_object_name = 'article_list'
    # 设定每页显示的文章数量，这个是内置视图函数自带的
    paginate_by = 10
    def get_queryset(self):
        # 返回按照创建时间逆排序的前5个
        return Article.objects.filter(status='p').order_by('-create_date')


class TimelineView(generic.ListView):

    template_name = 'blog/timeline.html'
    context_object_name = 'timeline_list'

    def get_queryset(self):
        return Timeline.objects.all()

class DetailView(generic.DetailView):
    model = Article
    pk_url_kwarg = 'article_id'
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.filter(status='p')

    def get_object(self):
        obj = super(DetailView,self).get_object()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        obj.body = md.convert(obj.body)
        obj.toc = md.toc
        return obj

    def get_context_data(self, **kwargs):
        article = self.get_object()
        article.update_views()
        context_data = super(DetailView,self).get_context_data()
        return context_data
