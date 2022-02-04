from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.email}'
