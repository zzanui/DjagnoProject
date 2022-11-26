from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from common.forms import UserForm,ProfileForm
from django.contrib.auth.decorators import login_required

from .models import Profile

#회원가입
def singup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            Profile.objects.create(user=user_profile) #프로필 생성
            
            username = form.cleaned_data.get('username') #form.cleaned_data.get //개별적으로 값을 얻고 싶을 경우 사용
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username = username,password=raw_password)#사용자 인증
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')#로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(request,'common/signup.html',{'form':form})
# Create your views here.


#프로필 조회
@login_required(login_url="common:login")
def profile_detail(request,user_id):
    profile = get_object_or_404(Profile,user_id = user_id)#로그인중인 아이디랑 프로필유저아이디를 비교하여 같은것을 가져온다
    context = {"profile":profile}
    return render(request,"common/profile_detail.html",context)







#프로필수정
@login_required(login_url="common:login")
def profile_modify(request,profile_id):
    
    profile = get_object_or_404(Profile,pk = profile_id)
    
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = request.user
            profile.save()
            return redirect("common:profile_modify",profile_id = profile.id)
    else:
        form = ProfileForm(instance=profile)
    context = {'form':form}
    return render(request,"common/profile_modify.html")