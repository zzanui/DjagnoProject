from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from common.forms import UserForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile,Follow,User

#회원가입
def singup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            username = form.cleaned_data.get('username') #form.cleaned_data.get //개별적으로 값을 얻고 싶을 경우 사용
            
            Profile.objects.create(user=user_profile,nickname=username) #프로필 생성
            
            Follow.objects.create(user = user_profile)#팔로우목록 생성
            
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username = username,password=raw_password)#사용자 인증
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')#로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(request,'common/signup.html',{'form':form})



#프로필 조회
@login_required(login_url="common:login")
def profile_detail(request,user_id):
    profile = get_object_or_404(Profile,user_id = user_id)#로그인중인 아이디랑 프로필유저아이디를 비교하여 같은것을 가져온다
    context = {"profile":profile}
    return render(request,"common/profile_detail.html",context)



#프로필수정
@login_required(login_url="common:login")
def profile_modify(request,user_id):
    
    profile = get_object_or_404(Profile,user_id = user_id)

    if request.user.pk != profile.user_id:
        messages.error(request,'수정권한이 없습니다.')
        return redirect("common:profile_detail",user_id = profile.user_id)        
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():

            profile = form.save(commit=False)
            
            profile.save()
            return redirect("common:profile_detail",user_id = profile.user.id)
    else:
        form = ProfileForm(instance=profile)
    context = {'form':form}
    return render(request,"common/profile_modify.html",context)



#팔로우 목록
@login_required(login_url="common:login")
def follow_list(request,user_id):
    follow = get_object_or_404(Follow,user_id=user_id)
    userList = User.objects.exclude(pk=request.user.pk)#자기자신을 재외하고 불러옴
    
    context = {"follow" : follow , "userList" : userList}
    
    return render(request,"common/follow_list.html",context)
    
    
    
#팔로우
@login_required(login_url="common:login")
def following(request,to_user_id):
    print(request)
    
    to_user = get_object_or_404(User,pk = to_user_id)
    followUser = get_object_or_404(Follow,user = request.user)
    
    followUser.to_user.add(to_user)
    
    
    return redirect('common:follow_list',user_id = request.user.id)
    
#언팔로우
@login_required(login_url="common:login")
def unFollowing(request,to_user_id):
    to_user = get_object_or_404(User,pk = to_user_id)
    followUser = get_object_or_404(Follow,user = request.user)
    
    followUser.to_user.remove(to_user)
    
    return redirect('common:follow_list',user_id = request.user.id)
        
    
    
    


    
    
    
    
    