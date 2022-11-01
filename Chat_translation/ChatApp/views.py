from django.shortcuts import render

def index(request):
    return render(request, "chat/html/index.html")
# Create your views here.

def room(request,room_name):
   return render(request,"chat/html/room.html",{
    "room_name": room_name
    })
   
def test(request):
    return render(request,"chat/html/test.html")
    
