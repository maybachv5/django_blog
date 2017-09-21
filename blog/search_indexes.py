# -*- coding: utf-8 -*-

from haystack import indexes
from .models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # 关联文章的状态，不然视图中不能拿来用
    status = indexes.CharField(model_attr='status')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        # 只对发表的文章进行索引，每次更新文章自动更新索引
        return self.get_model().objects.filter(status='p')

