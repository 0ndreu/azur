import django_filters
from .models import WebPage


class PageFilter(django_filters.FilterSet):

    class Meta:
        model = WebPage
        fields = {
            'visited': ['lt', 'gt'],
            'tag': ['icontains'],
            'domain': ['exact'],
            'size': ['lte'],
        }

