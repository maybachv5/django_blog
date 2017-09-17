from django.db import models
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    name = models.CharField('文章标签',max_length=15)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_article_list(self):
        '''返回当前标签下所有发表的文章列表'''
        return Article.objects.filter(tags=self,status='p')


class Category(models.Model):
    name = models.CharField('文章分类',max_length=15)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_article_list(self):
        return Article.objects.filter(category=self,status='p')


class Article(models.Model):

    IMG_LINK = 'http://ovyn3jt7b.bkt.clouddn.com/img04.jpg'

    STATUS_CHOICE = (
        ('d','草稿'),
        ('p','发表'),
    )
    status = models.CharField('文章状态',max_length=1,default='d',choices=STATUS_CHOICE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='作者')
    title = models.CharField(max_length=30,verbose_name='文章标题')
    summary = models.TextField('文章摘要',max_length=200,default='文章摘要是用来展示的，请务必填写...')
    body = models.TextField(verbose_name='文章内容')
    img_link = models.CharField('图片地址',default=IMG_LINK,max_length=150)
    create_date = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    views = models.IntegerField('阅览量',default=0)
    comments = models.IntegerField('评论数',default=0)

    category = models.ForeignKey(Category,verbose_name='文章分类',blank=True,null=True,on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.title[:20]

    def update_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def update_comments(self):
        self.comments += 1
        self.save(update_fields=['comments'])

    def get_pre(self):
        return Article.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return Article.objects.filter(id__gt=self.id).order_by('id').first()


