from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


# 게시글
class Article(models.Model):
    # 글자수 제한
    title = models.CharField(max_length=200)
    # 글자 수 제한 없음
    content = models.TextField()
    create_date = models.DateField()
    modify_date = models.DateField(null=True,blank=True)
    #작성자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='author_article')
    #추천
    voter = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='voter_article')


    def __str__(self):
        return self.title

# 댓글
class Comment(models.Model):
    #작성자
    # 게시글 삭제시 동시에 같이 삭제//on_delete=models.CASCADE
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='author_comment')
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
   
    # blank=True는 form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 된다는 의미
    modify_date = models.DateField(null=True,blank=True)
    #추천
    voter = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='voter_comment')
