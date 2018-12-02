from django.conf.urls import url

from .views import GetEventsByCategory, GetAllEvents, GetWeekendEvents, GetFreeEvents

urlpatterns = [
    url(r'^allEvents/$', GetAllEvents, name='activate'),
    url(r'^particularEvents/(?P<category>[\w|\W]+)/$', GetEventsByCategory, name='activate'),
    url(r'^weekendEvents/$', GetWeekendEvents, name='activate'),
    url(r'^freeEvents/$', GetFreeEvents, name='activate'),
]