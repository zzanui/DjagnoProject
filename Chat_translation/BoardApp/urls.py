from django.urls import path
from . import views

app_name = 'BoardApp'

urlpatterns = [

    
    path('',views.index,name = 'index'),
    path("board/<int:article_id>/",views.detail,name='detail'),
    path('comment/create/<int:article_id>/', views.comment_create, name='comment_create'),
    path('board/create/',views.article_create,name="article_create"),
    path('article/modify/<int:article_id>/',views.article_modify,name="article_modify"),
    path('article/delete/<int:article_id>/',views.article_delete,name="article_delete"),
    path('comment/modify/<int:comment_id>',views.comment_modify,name="comment_modify"),
]