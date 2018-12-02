from event.models import Event
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import datetime


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

#helper functions
def toWordMonth(fullDate):

    data = dateParser(fullDate)
    month = data[0]
    wordedMonth = this.monthNumToWordDict[month]
    return wordedMonth


def getDay(fullDate):
    data = dateParser(fullDate)
    day = data[1]
    return day

def weekendDaysCalculator(currMonth, currDayOfWeek, currDayNum, currYear):
    
    monthDayDict= {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    } 

    SatMonth = 0
    SatDay = 0
    SatYear = 0
    SunMonth = 0
    SunDay = 0
    SunYear = 0
    
    numDaysAwaySat = 6-currDayOfWeek
    numDaysAwaySun = 7-currDayOfWeek
    newMonth = currMonth
    newYear = currYear
    totalNumDaysOfMonth = monthDayDict[currMonth]
    '''
    print(numDaysAwaySat)
    print(numDaysAwaySun)
    print(newMonth)
    print(newYear)
    print(totalNumDaysOfMonth)
    '''
    
    for i in range(numDaysAwaySun+1):
        
        if int(currDayNum) == int(totalNumDaysOfMonth):

            currDayNum = 1
            newMonth = newMonth + 1
            if newMonth == 13:
                newMonth = 1
                newYear = newYear + 1
                if newYear == 100:
                    newYear = "00"

        if currDayOfWeek == 6:
            SatMonth = newMonth
            SatDay = currDayNum
            SatYear = newYear
        
        if currDayOfWeek == 0:
            SunMonth = newMonth
            SunDay = currDayNum
            SunYear = newYear
        
        else:
            currDayNum = currDayNum + 1
            currDayOfWeek = currDayOfWeek + 1
            if currDayOfWeek == 7:
                currDayOfWeek = 0
    
    return [str(SatMonth), str(SatDay), str(SatYear), str(SunMonth), str(SunDay), str(SunYear)]

def dateParser(theDate):
    #print("The date given is")
    #print(theDate)
    begin = 0
    data = []
    
    for i in range(len(theDate)):
        if theDate[i] == "-":
            #print("found dash")
            substringer = theDate[begin: i]
            begin = i+1
            data.append(substringer)
        
    substringer = theDate[begin: len(theDate)]
    data.append(substringer)
    #print("the data is")
    #print(data)
    return data

def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday', 
              'Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday']
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365                  
    # leap year correction    
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek %= 7
    return dayOfWeek, week[dayOfWeek]

@csrf_exempt
def GetWeekendEvents(request):

    monthNumToWordDict = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    
    numDayOfWeekDict = {
        0: "Sun",
        1: "Mon",
        2: "Tues",
        3: "Wed",
        4: "Thur",
        5: "Fri",
        6: "Sat"
    }

    try:
        data = Event.objects.all()
        allEvents = []

        for i in data:
            allEvents.append(i.toJSON())

        x = datetime.datetime.today().strftime('%m-%d-%y')
        data = dateParser(str(x))
        if data[1][0] == "0":
            data[1] = data[1][1:]
        #print(data)

        fullYear = 2000 + int(data[2])

        month = int(data[0])
        day = int(data[1])
        year = int(data[2])
        dayOfWeek = weekDay(fullYear, month, day)[0]
        #print(dayOfWeek)

        weekendDateData = weekendDaysCalculator(month, dayOfWeek, day, year)
        #print(weekendDateData)

        weekendEventsList = []

        for i in range(len(allEvents)):
            addedToWeekendList = False
            anEvent = allEvents[i]

            dateData = dateParser(anEvent['Date'])
            #dateData[0] = month
            #dateData[1] = day
            #dateData[2] = year
            
            #event takes place this Saturday
            if ((str(dateData[0]) == weekendDateData[0]) and (str(dateData[1]) == weekendDateData[1]) and (str(dateData[2]) == weekendDateData[2]) and (addedToWeekendList == False)):
                weekendEventsList.append(anEvent)
                addedToWeekendList = True

            #event takes place this Sunday
            if ((str(dateData[0]) == weekendDateData[3]) and (str(dateData[1]) == weekendDateData[4]) and (str(dateData[2]) == weekendDateData[5]) and (addedToWeekendList == False)):
                weekendEventsList.append(anEvent)
                addedToWeekendList = True

        print(weekendEventsList)

        return JsonResponse({"These are all of the weekend events": weekendEventsList})

    except:
        print("Failed")

@csrf_exempt
def GetWeekendEvents(request):

    monthNumToWordDict = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    
    numDayOfWeekDict = {
        0: "Sun",
        1: "Mon",
        2: "Tues",
        3: "Wed",
        4: "Thur",
        5: "Fri",
        6: "Sat"
    }

    try:
        data = Event.objects.all()
        allEvents = []

        for i in data:
            allEvents.append(i.toJSON())

        x = datetime.datetime.today().strftime('%m-%d-%y')
        data = dateParser(str(x))
        if data[1][0] == "0":
            data[1] = data[1][1:]
        #print(data)

        fullYear = 2000 + int(data[2])

        month = int(data[0])
        day = int(data[1])
        year = int(data[2])
        dayOfWeek = weekDay(fullYear, month, day)[0]
        #print(dayOfWeek)

        weekendDateData = weekendDaysCalculator(month, dayOfWeek, day, year)
        #print(weekendDateData)

        weekendEventsList = []

        for i in range(len(allEvents)):
            addedToWeekendList = False
            anEvent = allEvents[i]

            dateData = dateParser(anEvent['Date'])
            #dateData[0] = month
            #dateData[1] = day
            #dateData[2] = year
            
            #event takes place this Saturday
            if ((str(dateData[0]) == weekendDateData[0]) and (str(dateData[1]) == weekendDateData[1]) and (str(dateData[2]) == weekendDateData[2]) and (addedToWeekendList == False)):
                weekendEventsList.append(anEvent)
                addedToWeekendList = True

            #event takes place this Sunday
            if ((str(dateData[0]) == weekendDateData[3]) and (str(dateData[1]) == weekendDateData[4]) and (str(dateData[2]) == weekendDateData[5]) and (addedToWeekendList == False)):
                weekendEventsList.append(anEvent)
                addedToWeekendList = True

        #print(weekendEventsList)

        return JsonResponse({"These are all of the weekend events": weekendEventsList})

    except:
        print("Failed")


@csrf_exempt
def GetFreeEvents(request):

    try:
        data = Event.objects.all()
        allEvents = []

        for i in data:
            allEvents.append(i.toJSON())

        freeEventsList = []

        for i in range(len(allEvents)):
            anEvent = allEvents[i]
            if (anEvent['AdmissionFee'] == 0):
                freeEventsList.append(anEvent)

        print(freeEventsList)

        return JsonResponse({"These are all of the free events": freeEventsList})

    except:
        print("Failed")


