# form은 필수 파라미터 값이 누락 되지 않았는지, 파라미터 형식이 적절한지를 검증할 목적으로 사용된다
# 그 외에 html을 자동으로 생성하거나 폼에 연결된 모델을 이용하여 데이터를 저장하는 기능도 있다.
from django import forms
from BoardApp.models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
        # widgets = {
        #     'title' : forms.TextInput(attrs={'class' : 'form-control'}),
        #     'content' : forms.Textarea(attrs={'class':'form-control','rows':'10'}),
        # }
        labls = {
            'title' : "제목",
            'content' : "내용",
        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content':'답변내용',
        }
