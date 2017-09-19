from django.shortcuts import render

from .models import Article,Tag,Category,Timeline
from django.views import generic
# Create your views here.


def homeview(request):
    return render(request,'blog/index.html')


class TimelineView(generic.ListView):

    template_name = 'blog/timeline.html'
    context_object_name = 'timeline_list'

    def get_queryset(self):
        return Timeline.objects.all()
