from django.shortcuts import render
from .models import Event, Take
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
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
    fields = ['image', 'title', 'description', 'takes']
    success_url = '/events'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/events/' + str(self.object.pk))


class EventUpdate(UpdateView):
    model = Event
    fields = ['image', 'title', 'description', 'takes']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/events/' + str(self.object.pk))

class EventDelete(DeleteView):
    model = Event
    success_url = '/events'

# user profile view
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    events = Event.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'events': events})




class TakeCreate(CreateView):
    model = Take
    fields = '__all__'

class TakeUpdate(UpdateView):
    model = Take
    fields = ['opinion']

class TakeDelete(DeleteView):
    model = Take
    success_url = '/takes'


def takes_index(request):
    takes = Take.objects.all()
    return render(request, 'takes/index.html', { 'takes': takes })

def takes_detail(request, take_id):
    take = Take.objects.get(id=take_id)
    return render(request, 'takes/detail.html', {'take': take})

# login view
def login_view(request):
    # we can use the same view for multiple HTTP requests
    # this can be done with a simple if statement
    if request.method == 'POST':
        # handle post request
        # if its a post we want to authenticate the user with username and pw
        form = LoginForm(request.POST)
        # we validate the form data
        if form.is_valid():
            # get the username and password and save them to variables
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            # using djangoa built in authenticate method
            user = authenticate(username = u, password = p)
            # if you found a user with matching credentials
            if user is not None:
                # if that user has not been disabled  by admin
                if user.is_active:
                    # then we use djangos built in login function 
                    login(request, user)
                    return HttpResponseRedirect('/user/' + str(user.username))
                else: 
                    print('this account has been disabled')
            else:
                print('the username or password is incorrect')
    else:
        # if request is a get, we render the login page
        form = LoginForm()
        return render(request, 'login.html', {'form': form})