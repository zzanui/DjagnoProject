from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from common.models import Profile


# error
# Manager isn't available; 'auth.User' has been swapped for 'common.User' 
from django.contrib.auth import get_user_model
User = get_user_model()

class UserForm(UserCreationForm):
    
    name = forms.CharField(label="이름")
    nickname = forms.CharField(label="닉네임")
    email = forms.EmailField(label="이메일")
    

    class Meta:
        model = User
        fields = ['username','password1','password2',"name","nickname",'email']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img','profile_content']
        labels = {
            'profile_img' : '프로필이미지',
            'profile_content' : '프로필소개글',
        }