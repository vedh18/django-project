from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id' : 1, 'name' : 'SpeakJS'}, 
    {'id' : 2, 'name' : 'The Coding Den'},
    {'id' : 3, 'name' : 'Programmer Humor'},
]

def home(request):
    variables = {'rooms' : rooms}
    return render(request, 'home.html', variables)

def room(request, pk):
    return render(request, 'room.html')
