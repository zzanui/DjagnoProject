
from pydoc import pager
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ArticleForm,CommentForm
from .models import Article
from django.core.paginator import Paginator

# Create your views here.
def index(request):#게시판메인
    page = request.GET.get('page', '1') #페이지값을 가져올때 디폴트url 1
    article_list = Article.objects.order_by('-create_date')#작성일 기준으로 정렬
    paiginator = Paginator(article_list,10)#페이지당 게시글 10개씩 보여주기
    page_obj = paiginator.get_page(page)#1페이지를 보여줘라
    context = {'article_list' : page_obj}
    return render(request,"board/article_list.html",context)


def detail(request,article_id):#상세보기
    article = get_object_or_404(Article, pk = article_id)
    context = {"article" : article}
    return render(request,"board/article_detail.html",context)


def comment_create(request,article_id):#댓글등록
    article = get_object_or_404(Article, pk = article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.article = article
            comment.save()
            return redirect('BoardApp:detail',article_id=article.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
            
    context = {'article' : article, 'form' : form}
    return render(request,'board/article_detail.html',context)


def article_create(request):#게시글등록
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.create_date = timezone.now()
            article.save()
            return redirect('BoardApp:index')
            
    else:
        form = ArticleForm()
        
    context = {'form':form}
    return render(request,'board/article_form.html',context)