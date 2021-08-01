from django.urls import path
from . import views

urlpatterns = [
    path('add-Event/', views.addevent, name='addevent'),
    path('show-Event/', views.showevent, name='showevents'),
    path('ho/', views.homeview),
]