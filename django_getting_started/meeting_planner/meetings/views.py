from django.shortcuts import render, get_object_or_404
from .models import Meeting, Room

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    #One way is Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms(request):
    return render(request, "meetings/room_detail.html",
                  {"rooms": Room.objects.all()})
