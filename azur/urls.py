from django.urls import path
from .views import *

urlpatterns = [
    path('', WebPagesViewList.as_view(), name='home'),
    path('v2', WebView.as_view(), name='home2')
]