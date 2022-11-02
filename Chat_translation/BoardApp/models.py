from importlib.resources import contents
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# 게시글
class Article(models.Model):
    # 글자수 제한
    title = models.CharField(max_length=200)
    # 글자 수 제한 없음
    content = models.TextField()
    create_date = models.DateField()
    
    def __str__(self):
        return self.title

# 댓글
class Comment(models.Model):
    # 게시글 삭제시 동시에 같이 삭제//on_delete=models.CASCADE
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    
