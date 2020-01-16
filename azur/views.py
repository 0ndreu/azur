from django.views.generic import ListView
from .models import WebPage
from django.db.models import Q
from .filters import *


class WebPagesViewList(ListView):
    model = WebPage
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PageFilter(self.request.GET, queryset=self.get_queryset())
        return context

