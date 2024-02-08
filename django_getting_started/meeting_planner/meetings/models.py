from datetime import time
from django.db import models

class Meeting(models.Model):
    #The database fields
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    #Needed double underscores here
    #Displays friendly titles in the admin interface
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"