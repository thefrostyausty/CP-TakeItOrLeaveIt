from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events_index, name='events_index'),
    path('events/<int:event_id>/', views.events_show, name='events_show')
]