from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
from meetings.models import Room

def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})
#The message is rendered using the dictionary - see html file for placeholders - dynamic pages

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hello I'm here")

def rooms(request):
    return render(request, "website/room_detail.html",
                  {"rooms": Room.objects.all()})