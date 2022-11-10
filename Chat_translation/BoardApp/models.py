from importlib.resources import contents
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 게시글
class Article(models.Model):
    # 글자수 제한
    title = models.CharField(max_length=200)
    # 글자 수 제한 없음
    content = models.TextField()
    create_date = models.DateField()
    modify_date = models.DateField(null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_article')
    voter = models.ManyToManyField(User,related_name='voter_article')


    def __str__(self):
        return self.title

# 댓글
class Comment(models.Model):
    # 게시글 삭제시 동시에 같이 삭제//on_delete=models.CASCADE
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_comment')
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    # blank=True는 form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 된다는 의미
    modify_date = models.DateField(null=True,blank=True)
    voter = models.ManyToManyField(User,related_name='voter_comment')
