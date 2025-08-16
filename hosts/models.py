from django.db import models
from django.contrib.auth.models import User

class EventDetails(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "events")
    name = models.CharField(max_length=25, blank=False, null=False)
    place = models.CharField(max_length=25, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    seats = models.IntegerField(blank=False, null=False)
    banner = models.ImageField(upload_to='hosts/', blank=False, null=False)
