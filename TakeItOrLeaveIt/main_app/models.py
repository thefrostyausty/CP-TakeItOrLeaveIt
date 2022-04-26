from django.db import models

# Create your models here.

class Event(models.Model):
    image = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title