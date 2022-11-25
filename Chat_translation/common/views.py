from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from common.forms import UserForm


def singup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #form.cleaned_data.get //개별적으로 값을 얻고 싶을 경우 사용
            raw_password = form.cleaned_data.get('password1')
            
            user = authenticate(username = username,password=raw_password)#사용자 인증
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')#로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(request,'common/signup.html',{'form':form})
# Create your views here.
