from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Article

def index(request):#게시판메인
    page = request.GET.get('page', '1') #페이지값을 가져올때 디폴트url 1
    kw = request.GET.get('kw', '')  # 검색어
    article_list = Article.objects.order_by('-create_date')#작성일 기준으로 정렬
    if kw:
        article_list = article_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(comment__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(comment__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    
    paiginator = Paginator(article_list,10)#페이지당 게시글 10개씩 보여주기
    page_obj = paiginator.get_page(page)#1페이지를 보여줘라
    context = {'article_list' : page_obj, 'page': page, 'kw': kw}
    return render(request,"board/article_list.html",context)


def detail(request,article_id):#상세보기
    article = get_object_or_404(Article, pk = article_id)
    context = {"article" : article}
    return render(request,"board/article_detail.html",context)