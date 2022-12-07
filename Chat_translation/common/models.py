#models.py
from django.db import models
from django.contrib.auth.models import AbstractUser 

#auth의 유저 상속
class User(AbstractUser):
    """
        이름
        이메일
    """
    

    name = models.CharField(max_length=15)
    email = models.EmailField()
    
    
    class Meta:
        db_table = "User"
        
        
    def __str__(self):
        return self.username
    
#models.py
#프로필
class Profile(models.Model):
    """    
        유저아이디
        닉네임
        프로필이미지
        프로필소개글
    """

    user = models.OneToOneField(User,on_delete=models.CASCADE)#유저와 1:1 join
    nickname = models.CharField(max_length=15,unique=True,null=True)
    profile_img = models.ImageField(blank=True,null=True,upload_to="images/")
    profile_content = models.TextField(blank=True)


#친구목록
class Follow(models.Model):
    """
    유저 
    친구유저
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
    to_user   = models.ManyToManyField(User,related_name="to_user")
    