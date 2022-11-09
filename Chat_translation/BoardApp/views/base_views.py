from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Article

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