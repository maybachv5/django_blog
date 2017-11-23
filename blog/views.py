from .models import Article, Tag, Category, Timeline
from django.views import generic
# Create your views here.
import markdown
from markdown.extensions.toc import TocExtension  # 锚点的拓展
from django.utils.text import slugify  # 这个目测是URL支持中文的拓展
from haystack.generic_views import SearchView  # 导入搜索视图
from django.shortcuts import get_object_or_404, render

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
        context_data = super(DetailView, self).get_context_data()
        return context_data


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

def findjob(request):
    return render(request,'blog/findjob.html')

