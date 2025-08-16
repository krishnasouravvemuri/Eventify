from django.db import models
import uuid
from hosts.models import EventDetails
from django.contrib.auth.models import User

class MemberDetails(models.Model):
    event = models.ForeignKey(EventDetails , related_name="registrations" , on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="event_registrations", on_delete=models.CASCADE)
    no_of_members = models.PositiveIntegerField(default = 1)
    member_name = models.CharField(null=False , blank=False)
    registration_code = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        if not self.registration_code:
            self.registration_code = str(uuid.uuid4()).replace('-', '')[:12].upper()
        super().save(*args, **kwargs)