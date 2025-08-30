from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


rooms = [
    {'id':1,"name":"Lets learn Python"},
    {'id':2,"name":"Lets learn Django"},
    {'id':3,"name":"Lets learn JavaScript"}
]



def home(request):
    return render(request,'home.html',{"rooms":rooms})

def room(request):
    return render(request,'room.html')