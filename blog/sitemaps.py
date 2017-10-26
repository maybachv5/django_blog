# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from .models import Article, Category, Tag


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Article.objects.filter(status='p')

    def lastmod(self, obj):
        return obj.update_date


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        l = []
        cates = Category.objects.all()
        for each in cates:
            if each.article_set.filter(status='p'):
                l.append(each)
        return l

    def lastmod(self, obj):
        return obj.article_set.filter(status='p')[0].create_date


class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        l = []
        cates = Tag.objects.all()
        for each in cates:
            if each.article_set.filter(status='p'):
                l.append(each)
        return l

    def lastmod(self, obj):
        return obj.article_set.filter(status='p')[0].create_date
