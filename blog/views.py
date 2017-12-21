from .models import Article, Tag, Category, Timeline, Silian
from django.views import generic
# Create your views here.
import markdown
from markdown.extensions.toc import TocExtension  # 锚点的拓展
from django.utils.text import slugify  # 这个目测是URL支持中文的拓展
from haystack.generic_views import SearchView  # 导入搜索视图
from django.shortcuts import get_object_or_404, render
import time

def Aboutview(request):
    return render(request,'blog/about.html',context={})

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(status='p')


class TimelineView(generic.ListView):
    template_name = 'blog/timeline.html'
    context_object_name = 'timeline_list'

    def get_queryset(self):
        return Timeline.objects.all()


class DetailView(generic.DetailView):
    model = Article
    slug_url_kwarg = 'slug'
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        queryset = super(DetailView, self).get_queryset()
        return queryset.filter(status='p')

    def get_object(self):
        obj = super(DetailView, self).get_object()
        # 设置浏览量增加时间判断,同一篇文章两次浏览超过2小时才重新统计阅览量,作者浏览忽略
        u = self.request.user
        ses = self.request.session
        the_key = 'is_read_{}'.format(obj.id)
        is_read_time = ses.get(the_key)
        if not is_read_time:
            if u != obj.author:
                obj.update_views()
                ses[the_key] = time.time()
        else:
            now_time = time.time()
            t = now_time - is_read_time
            if t > 7200 and u != obj.author:
                obj.update_views()
                ses[the_key] = time.time()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        obj.body = md.convert(obj.body)
        obj.toc = md.toc
        return obj

class CategoryView(generic.ListView):
    model = Article
    template_name = 'blog/category_and_tag.html'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        cate = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return super(CategoryView, self).get_queryset().filter(category=cate, status='p')

    def get_context_data(self, **kwargs):
        cate = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context_data = super(CategoryView, self).get_context_data()
        context_data['search_tag'] = '分类'
        context_data['search_name'] = cate
        return context_data


class TagView(generic.ListView):
    model = Article
    template_name = 'blog/category_and_tag.html'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        return super(TagView, self).get_queryset().filter(tags=tag, status='p')

    def get_context_data(self, **kwargs):
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        context_data = super(TagView, self).get_context_data()
        context_data['search_tag'] = '标签'
        context_data['search_name'] = tag
        return context_data


# 重写搜索视图，可以增加一些额外的参数，且可以重新定义名称
class MySearchView(SearchView):
    context_object_name = 'search_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        # 这个过滤有问题，并没有把status='d'的过滤掉，这是个bug目前不得解
        return queryset.filter(status='p')

class SilianView(generic.ListView):
    model = Silian
    template_name = 'silian.xml'
    context_object_name = 'badurls'

