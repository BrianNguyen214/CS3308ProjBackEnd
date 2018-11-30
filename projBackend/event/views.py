from event.models import Event
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def GetEventsByCategory(request, category):

    allArticles = Article.objects.all()
    theArticle = Article()
    
    try:
        data = Event.objects.get(Category=category)
        print(theParticularEvents)

        data = Article.objects.all()
        theEvents = []

        for event in theParticularEvents:
            theEvents.append(event.toJSON())

        return JsonResponse({"These are the events": theEvents})

    except:
        print("Failed")
        return HttpResponse("It failed")

    return HttpResponse("It really failed")
