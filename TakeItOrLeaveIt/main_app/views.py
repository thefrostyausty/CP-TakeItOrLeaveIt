from curses.ascii import HT
from django.shortcuts import render
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

class Event:
    def __init__(self, title, description):
        self.title = title
        self.description = description

events = [
    Event('Oscars Slap', 'Will Smith in the heat of the moment, attacks Chris Rock'),
    Event('Kanye Interrupts Taylor Swift', 'Kanye explains to everyone that Beyoncé had the best video of all time'),
    Event("'Say My Name' music video debuts with a surprise", "The newest music video released by Destiny's Child showed two new members to the surprise of many")
]

def events_index(request):
    return render(request, 'events/index.html', {'events': events})