from django.db import models
from django.conf import settings
import markdown
import emoji
from django.shortcuts import reverse
from django.utils.text import slugify


# Create your models here.

# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=15)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_article_list(self):
        '''返回当前标签下所有发表的文章列表'''
        return Article.objects.filter(tags=self, status='p')

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'slug': self.slug})

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.slug)
    #     super(Tag,self).save()

# 文章分类
class Category(models.Model):
    name = models.CharField('文章分类', max_length=15)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    def get_article_list(self):
        return Article.objects.filter(category=self, status='p')

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.slug)
    #     super(Category,self).save()

# 文章
class Article(models.Model):
    IMG_LINK = settings.DEFAULT_IMG_LINL

    STATUS_CHOICE = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    status = models.CharField('文章状态', max_length=1, default='p', choices=STATUS_CHOICE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')
    title = models.CharField(max_length=100, verbose_name='文章标题')
    summary = models.TextField('文章摘要', max_length=200, default='文章摘要是用来展示的，请务必填写...')
    body = models.TextField(verbose_name='文章内容')
    img_link = models.CharField('图片地址', default=IMG_LINK, max_length=255)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    views = models.IntegerField('阅览量', default=0)
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(Category, verbose_name='文章分类', blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def body_to_markdown(self):
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def update_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_pre(self):
        return Article.objects.filter(id__lt=self.id,status='p').order_by('-id').first()

    def get_next(self):
        return Article.objects.filter(id__gt=self.id,status='p').order_by('id').first()

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.slug)
    #     super(Article,self).save()

# 时间线
class Timeline(models.Model):
    COLOR_CHOICE = (
        ('primary', '基本-蓝色'),
        ('success', '成功-绿色'),
        ('info', '信息-天蓝色'),
        ('warning', '警告-橙色'),
        ('danger', '危险-红色')
    )
    SIDE_CHOICE = (
        ('L', '左边'),
        ('R', '右边'),
    )
    STAR_NUM = (
        (1,'1颗星'),
        (2,'2颗星'),
        (3,'3颗星'),
        (4,'4颗星'),
        (5,'5颗星'),
    )
    side = models.CharField('位置', max_length=1, choices=SIDE_CHOICE, default='L')
    star_num = models.IntegerField('星星个数',choices=STAR_NUM,default=3)
    icon = models.CharField('图标', max_length=50, default='glyphicon glyphicon-pencil')
    icon_color = models.CharField('图标颜色', max_length=20, choices=COLOR_CHOICE, default='info')
    title = models.CharField('标题', max_length=100)
    update_date = models.DateTimeField('更新时间')
    content = models.TextField('主要内容')

    class Meta:
        verbose_name = '时间线'
        verbose_name_plural = verbose_name
        ordering = ['update_date']

    def __str__(self):
        return self.title[:20]

    def title_to_emoji(self):
        return emoji.emojize(self.title,use_aliases=True)

    def content_to_markdown(self):
        # 先转换成emoji然后转换成markdown
        to_emoji_content = emoji.emojize(self.content,use_aliases=True)
        return markdown.markdown(to_emoji_content, extensions=[
            'markdown.extensions.extra',
        ])

# 幻灯片
class Carousel(models.Model):
    number = models.IntegerField('编号',help_text='编号决定图片播放的顺序')
    title = models.CharField('标题',max_length=20,blank=True,null=True,help_text='标题可以为空')
    content = models.CharField('描述',max_length=80)
    img_url = models.CharField('图片地址',max_length=200)
    url = models.CharField('跳转链接',max_length=200,default='#',help_text='图片跳转的超链接，默认#表示不跳转')

    class Meta:
        verbose_name = '图片轮播'
        verbose_name_plural = verbose_name
        ordering = ['number','id']

    def __str__(self):
        return self.title


# 死链
class Silian(models.Model):
    badurl = models.CharField('死链地址',max_length=200,help_text='地址必须带http')
    remark = models.CharField('死链说明',max_length=50,blank=True,null=True)
    add_date = models.DateTimeField('提交日期',auto_now_add=True)

    class Meta:
        verbose_name = '死链'
        verbose_name_plural = verbose_name
        ordering = ['-add_date']

    def __str__(self):
        return self.badurl