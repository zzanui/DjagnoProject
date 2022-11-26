#models.py
from django.db import models
from django.contrib.auth.models import AbstractUser 

#auth의 유저 상속
class User(AbstractUser):
    """
        닉네임
        이름
        이메일
    """
    
    nickname = models.CharField(max_length=15,unique=True,null=True)
    name = models.CharField(max_length=15)
    email = models.EmailField()
    
    USERNAME_FIELD: 'nickname'
    
    class Meta:
        db_table = "User"
        
        
    def __str__(self):
        return self.email
    
#models.py
#프로필
class Profile(models.Model):
    """    
        유저아이디
        프로필이미지
        프로필소개글
    """

    user = models.OneToOneField(User,on_delete=models.CASCADE)#유저와 1:1 join
    profile_img = models.ImageField(blank=True,upload_to="images/")
    profile_content = models.TextField(blank=True)



    