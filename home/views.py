from django.shortcuts import render
from .models import Room
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
