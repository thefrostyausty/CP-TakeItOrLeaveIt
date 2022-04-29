from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
    



class Event(models.Model):
    # user comes from django, has prebuilt properties and methods
    #  we set up out forieng key reference
    # we tell it which model we're referring to (user)
    # the second argukent (on_delete) says to delete all resources that are
    # owned by the user
    # basically if user is deleted all resources associated with user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # takes = models.ManyToManyField(Take)


    def __str__(self):
        return self.title

class Take(models.Model):
    opinion = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.opinion
    
    def get_absolute_url(self):
        return reverse('takes_detail', kwargs={'take_id': self.id})

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    take = models.ForeignKey(Take, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment