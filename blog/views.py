from django.shortcuts import render

from .models import Article,Tag,Category
from django.views import generic
# Create your views here.


def homeview(request):
    return render(request,'blog/index.html')
