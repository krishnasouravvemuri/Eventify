from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    company_name = models.CharField(max_length = 100, blank = True, null = True)
    ROLE_CHOICES = [
        ('host', 'Host'),
        ('member', 'Member'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)