from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .spider_apis import *


# Create your views here.

def wordsearch(request):
    return render(request,'tools/wordsearch.html',context={})

@login_required
def wordsearch_api(request):
    word = request.GET.get('word')
    tb = TB_WordSearch(word)
    tb_results = tb.get_result()
    tm = TM_WordSearch(word)
    tm_results = tm.get_result()
    return JsonResponse({'tb_results':tb_results,'tm_results':tm_results})
