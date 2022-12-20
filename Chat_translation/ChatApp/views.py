from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def mainpage(request):
    return render(request, "chat/html/index.html")
# Create your views here.

def room(request, room_name):
    return render(request, 'chat/html/room.html', {"room_name": room_name})
   

    
