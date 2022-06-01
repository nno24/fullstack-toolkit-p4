from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone as tz
from datetime import date, time

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    people = models.IntegerField(default=2)
    date = models.DateField(default=tz.now)
    time = models.TimeField(default=time(18, 00))
    user = models.CharField(max_length=200, null=False, blank=False, default='guest')
    
    def __str__(self):
        return f'{self.name}  |  {self.people}  |  {self.date}  {self.time}'
