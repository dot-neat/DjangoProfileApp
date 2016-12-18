from django.db import models
import datetime
from django.utils import timezone


class PersonInfo(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField(unique=True,default="")   
    def __str__(self):
        return self.name  