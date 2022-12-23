from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from collections import Counter



from .models import Room,Message
from common.models import User,Profile

def mainpage(request):
    return render(request, "chat/html/index.html")
# Create your views here.

#채팅방보기
@login_required
def view_room(request: HttpRequest, room_name:str) -> HttpResponse:
    room_id = int(room_name)
    try:
        user_prifile = Profile.objects.get(user=request.user)
        return render(request,'chat/html/room.html',{
            "room_name": room_id,
            "user_prifile":user_prifile})
    except:
        return render(request,'chat/html/room.html')
    
    
   

#채팅방 생성
@login_required
def create_room(request: HttpRequest, user_id:int) -> HttpResponse:
    user1 = User.objects.get(id = request.user.id)
    user2 = User.objects.get(id = user_id)
    
    #1번,2번 유저가 참여한 모든 방을 가져옴
    find_room_qs = Room.objects.filter(user__in=[user1.id,user2.id])
    
    find_room_list=[]
    for find_room in find_room_qs:
        find_room_list.append(find_room.id)
    
    result = Counter(find_room_list)
    for key,value in result.items():
        if value >= 2:
            #기존에 채팅방이 존재할 경우 이동
            return redirect("ChatApp:view_room",room_name=str(key))
        
        
    roomname = 'test'
    room = Room.objects.create(name = roomname)
    room.user.add(user1,user2)
    room_id = room.id
    #기존에 채팅방이 존재하지 않을경우 이동
    return redirect("ChatApp:view_room",room_name=str(room_id))