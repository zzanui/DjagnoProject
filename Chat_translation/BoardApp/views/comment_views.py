
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..forms import CommentForm
from ..models import Article,Comment
# Create your views here.


#댓글등록
@login_required(login_url='common:login')#로그인이 필요한 함수가 초출되면 해당 주소로 이동
def comment_create(request,article_id):
    article = get_object_or_404(Article, pk = article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            
            comment = form.save(commit=False)
            comment.author = request.user #author 속성에 로그인 계정 저장
            comment.create_date = timezone.now()
            comment.article = article
            comment.save()
            return redirect('BoardApp:detail',article_id=article.id)
    else:
        form = CommentForm()
            
    context = {'article' : article, 'form' : form}
    return render(request,'board/article_detail.html',context)


#댓글 수정
@login_required(login_url="common:login")
def comment_modify(request,comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    if request.user != comment.author:
        messages.error(request,"수정권한이 없습니다.")
        return redirect("BoardApp:detail",comment_id=comment.id)
    if request.method == "POST":
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect("BoardApp:detail",article_id = comment.article.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment':comment,"form":form}
    return render(request,'board/comment_form.html',context)
    
#댓글 삭제
@login_required(login_url="common:login")
def comment_delete(request,comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    if request.user != comment.author:
        messages.error("삭제권한이 없습니다.")
    else:
        comment.delete()
    return redirect("BoardApp:detail",article_id=comment.article.id)

#댓글 추천
@login_required(login_url="common:login")
def comment_vote(request,comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    if request.user == comment.author:
        messages.error(request,"본인이 작성한 글은 추천이 불가능합니다.")
    else:
        comment.voter.add(request.user)
    return redirect("BoardApp:detail",article_id=comment.article.id)

    
    
    

    