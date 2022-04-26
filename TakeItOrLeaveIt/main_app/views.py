from curses.ascii import CR
from sre_constants import SUCCESS
from django.shortcuts import render
from .models import Event
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# def about(request):
#     return HttpResponse('<h1>I am Austin the developer</h1>')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# class Event:
#     def __init__(self, image, title, description):
#         self.image = image
#         self.title = title
#         self.description = description

# events = [
#     Event('Oscars Slap', 'Will Smith in the heat of the moment, attacks Chris Rock', 'this is a description'),
#     Event('Kanye Interrupts Taylor Swift', 'Kanye explains to everyone that Beyoncé had the best video of all time', 'another description'),
#     Event("'Say My Name' music video debuts with a surprise", "The newest music video released by Destiny's Child showed two new members to the surprise of many", 'descritption')
# ]

def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def events_show(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/show.html', {'event': event})

class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    success_url = '/events'


class EventUpdate(UpdateView):
    model = Event
    fields = ['image', 'title', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/events/' + str(self.object.pk))

class EventDelete(DeleteView):
    model = Event
    success_url = '/events'