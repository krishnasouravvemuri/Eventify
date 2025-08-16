from django import forms 
from .models import EventDetails

class HostEventForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ['name' , 'place' , 'date' , 'time' , 'seats' , 'banner']
