from datetime import time
from django.db import models

class Meeting(models.Model):
    #The database fields
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    #Needed double underscores here
    #Displays friendly titles in the admin interface
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
    
class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} is Room {self.room_number} on Floor {self.floor_number}"