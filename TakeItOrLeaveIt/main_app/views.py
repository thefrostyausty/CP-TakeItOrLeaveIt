from django.shortcuts import render
from .models import Event, Take, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse


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
    takes = Take.objects.filter(event = event_id)
    return render(request, 'events/show.html', {'event': event, 'takes': takes})

class EventCreate(CreateView):
    model = Event
    fields = ['image', 'title', 'description']
    success_url = '/events/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/events/' + str(self.object.pk))


class EventUpdate(UpdateView):
    model = Event
    fields = ['image', 'title', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/events/' + str(self.object.pk))

@method_decorator(login_required, name='dispatch')
class EventDelete(DeleteView):
    model = Event
    success_url = '/events'



# class Take:
#     def __init__(self, opinion):
#         self.opinion = opinion


# takes =[ 
#     Take('sdshdbhsdbhshsbhbdhd')
# ]

class TakeCreate(CreateView):
    model = Take
    fields = '__all__'

class TakeUpdate(UpdateView):
    model = Take
    fields = ['opinion']

@method_decorator(login_required, name='dispatch')
class TakeDelete(DeleteView):
    model = Take
    success_url = '/takes'

class CommentCreate(CreateView):
    model = Comment
    fields = '__all__'

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['comment']

class CommentDelete(DeleteView):
    model = Comment
    success_url = '/takes'

def comments_index(request):
    comment = Comment.objects.all()
    return render(request, 'takes/index.html', {'comments': comment })

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


# sign up view
def signup_view(request):
    # if the request is a POSt then sign them up
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/user/' + str(user.username))
    # if the request is a GET then show that form
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


# log out view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

# user profile view
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    events = Event.objects.filter(user=user)
    takes = Take.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'events': events, 'takes': takes})
    