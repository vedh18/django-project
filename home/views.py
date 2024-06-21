from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id' : 1, 'name' : 'SpeakJS'}, 
#     {'id' : 2, 'name' : 'The Coding Den'},
#     {'id' : 3, 'name' : 'Programmer Humor'},
# ]

def home(request):
    rooms = Room.objects.all()
    variables = {'rooms': rooms}
    return render(request, 'home.html', variables)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST) # Passing the user input into the Form object
        if form.is_valid():
            form.save()
            return redirect('home')

    variables = {'form' : form}
    return render(request, 'room_form.html', variables)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    variables = {'form' : form}
    return render(request, 'room_form.html', variables)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'delete.html', {'obj': room})