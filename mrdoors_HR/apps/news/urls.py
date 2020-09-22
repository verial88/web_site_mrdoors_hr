from django.conf.urls import url
from .views import NewsView, show_news, NewsList

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', NewsView.as_view(), name='news_detail'),
    url(r'^all/$', NewsList.as_view(), name='news_list'),
    url(r'^(?P<news_id>\d+)/$', show_news, name='news_id'),
    url(r'^(?P<news_id>\d+)/like/$', show_news, name='news_likes'),
]
