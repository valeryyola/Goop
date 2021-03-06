from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q)|
        Q(name__icontains =  q) |
        Q(description__icontains = q)
        )
    
    topics = Topic.objects.all()
    roomCount = rooms.count()
    context = {'rooms':rooms, 'topics':topics, 'room_count': roomCount}
    return render(request, 'base/home.html',context)


def room(request, pk):
    room = Room.objects.get(id = pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def roomForm(request):
    context = {'form': RoomForm}

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    context = {'form': form}
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html', {'obj':room})

