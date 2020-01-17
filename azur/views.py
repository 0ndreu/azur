from django.views.generic import ListView
from .models import WebPage
from django.db.models import Q, Count
from .filters import *


class WebPagesViewList(ListView):
    model = WebPage
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PageFilter(self.request.GET, queryset=self.get_queryset())
        return context


class WebView(ListView):
    model = WebPage
    template_name = 'index.html'

    def get_queryset(self):
        queryset = WebPage.objects.all()
        tag = self.request.GET.get('tag')
        domain = self.request.GET.get('domain')
        size = self.request.GET.get('size')
        load_code = self.request.GET.get('load_code')
        ch_tag = self.request.GET.get('ch_tag')
        ch_dom = self.request.GET.get('ch_dom')
        ch_lc = self.request.GET.get('ch_lc')
        if tag or domain or size or load_code is not None:
            if tag is not '':
                queryset = queryset.filter(tag__contains=tag)
            if domain is not '':
                queryset = queryset.filter(domain=domain)
            if size is not '':
                queryset = queryset.filter(size__lte=size)
            if load_code is not '':
                if 'XX' in str(load_code).upper():
                    queryset = queryset.filter(load_code__range=(int(load_code[0]) * 100, int(load_code[0]) * 100 + 99))
                else:
                    queryset = queryset.filter(load_code=load_code)
        if ch_tag == 't':
            queryset = queryset.values('tag').order_by('tag').annotate(count=Count('tag'))
        if ch_dom == 't':
            queryset = queryset.values('domain').order_by('domain').annotate(count=Count('domain'))
        if ch_lc == 't':
            queryset = queryset.values('load_code').order_by('load_code').annotate(count=Count('load_code'))
        return queryset
