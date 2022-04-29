from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events_index, name='events_index'),
    path('events/<int:event_id>/', views.events_show, name='events_show'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('comments/', views.comments_index, name='comments_index'),
    path('comments/create', views.CommentCreate.as_view(), name='comments_create'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    path('comments/<int:pk>/delete', views.CommentDelete.as_view(), name='comments_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('events/<int:event_id>/takes/', views.takes_index, name='takes_index'),
    path('takes/<int:take_id>/', views.takes_detail, name='takes_detail'),
    path('events/<int:event_id>/takes/create', views.TakeCreate.as_view(), name='takes_create'),
    path('takes/<int:pk>/update/', views.TakeUpdate.as_view(), name='takes_update'),
    path('takes/<int:pk>/delete', views.TakeDelete.as_view(), name='takes_delete'),
]