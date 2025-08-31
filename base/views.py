from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


rooms = [
    {'id':1,"name":"Lets learn Python"},
    {'id':2,"name":"Lets learn Django"},
    {'id':3,"name":"Lets learn JavaScript"}
]


def home(request):
    context = {"rooms":rooms}
    return render(request,'base/home.html',context)

def room(request, pk):
    room = None
    for i in rooms:
        
        if i['id'] == int(pk):
            room = i
            print(room)
    print('DEBUG room:', room)
    context = {'room': room}
    return render(request, 'base/room.html', context)