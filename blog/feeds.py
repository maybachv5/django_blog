# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from .models import Article

class AllArticleRssFeed(Feed):
    # 显示在聚会阅读器上的标题
    title = "Stopfollow 个人博客"
    # 跳转网址，为主页
    link = "/"
    # 描述内容
    description = "一个由Django搭建的个人博客,分享学习Python的一些心得。"
    # 需要显示的内容条目，这个可以自己挑选一些热门或者最新的博客
    # 我觉得可以为博客单独添加一个RSS的属性，is_rss代表推荐，然后按照这个去筛选需要RSS分享出来的博客
    def items(self):
        return Article.objects.all()[:20]

    # 显示的内容的标题,这个才是最主要的东西
    def item_title(self, item):
        return "【{}】{}".format(item.category,item.title)

    # 显示的内容的描述
    def item_description(self, item):
        return item.summary