from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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