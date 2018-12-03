from django.conf.urls import url

from .views import GetEventsByCategory, GetAllEvents, GetWeekendEvents, GetFreeEvents, GetSpecificEvent

urlpatterns = [
    url(r'^allEvents/$', GetAllEvents, name='activate'),
    url(r'^particularEvents/(?P<category>[\w|\W]+)/$', GetEventsByCategory, name='activate'),
    url(r'^weekendEvents/$', GetWeekendEvents, name='activate'),
    url(r'^freeEvents/$', GetFreeEvents, name='activate'),
    url(r'^specificEvent/(?P<token1>[0-9]+)/(?P<token2>[0-9]+)/(?P<token3>[\w|\W]+)/$', GetSpecificEvent, name='activate'),
]