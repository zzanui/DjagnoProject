from django.urls import path
from .views import comment_views,base_views,article_views

app_name = 'BoardApp'

urlpatterns = [

     # base_views.py
    path('',base_views.index,name = 'index'),
    path("board/<int:article_id>/",base_views.detail,name='detail'),
    
    # article_views
    path('board/create/',article_views.article_create,name="article_create"),
    path('article/modify/<int:article_id>/',article_views.article_modify,name="article_modify"),
    path('article/delete/<int:article_id>/',article_views.article_delete,name="article_delete"),
    
    # comment_views
    path('comment/create/<int:article_id>/', comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>',comment_views.comment_modify,name="comment_modify"),
    path('comment/delete/<int:commnet_id>',comment_views.comment_delete,name="comment_delete"),
]