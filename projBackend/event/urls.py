from django.conf.urls import url

from .views import GetEventsByCategory, GetAllEvents

urlpatterns = [
    url(r'^allEvents/$', GetAllEvents, name='activate'),
    url(r'^particularEvents/(?P<category>[\w|\W]+)/$', GetEventsByCategory, name='activate'),
]