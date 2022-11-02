from django.urls import path
from . import views

app_name = 'BoardApp'

urlpatterns = [

    
    path('',views.index,name = 'index'),
    path("board/<int:article_id>/",views.detail,name='detail'),
    path('create/<int:article_id>/', views.comment_create, name='comment_create'),
    path('board/create/',views.article_create,name="article_create"),
]