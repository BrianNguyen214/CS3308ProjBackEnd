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
    print(category)
    try:
        theParticularEvents = Event.objects.filter(Category=str(category))
        theEvents = []

        for event in theParticularEvents:
            theEvents.append(event.toJSON())

        return JsonResponse({"These are the events": theEvents})

    except:
        print("Failed")
        return HttpResponse("It failed")

    return HttpResponse("It really failed")

@csrf_exempt
def GetAllEvents(request):
    try:
        data = Event.objects.all()
        allEvents = []

        for i in data:
            allEvents.append(i.toJSON())

        return JsonResponse({"These are all of the events": allEvents})

    except:
        print("Failed")
