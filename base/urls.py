from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('room/<pk>/', views.room, name='room'),
    path('room-form', views.roomForm, name='room-form'),
    path('room-form/<pk>', views.updateRoom, name='update-room-form')


]