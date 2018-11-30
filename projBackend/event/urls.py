from django.conf.urls import url

from .views import GetEventsByCategory#s, SendArticles, GetImages, GetVideos, GetArticle

urlpatterns = [
    #url(r'^$', SendArticles, name='sendArticles'),
    #url(r'^images/(?P<article>[\w|\W]+)/$', GetImages, name='activate'),
    #url(r'^videos/(?P<article>[\w|\W]+)/$', GetVideos, name='activate'),
    url(r'^particularEvents/(?P<category>[\w|\W]+)/$', GetEventsByCategory, name='activate'),
    #url(r'^gettingArticle/(?P<token1>[0-9]+)/(?P<token2>[0-9]+)/(?P<token3>[\w|\W]+)/$', GetArticle, name='activate'),
]