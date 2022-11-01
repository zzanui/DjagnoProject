from django.urls import path
from . import views

app_name = 'BoardApp'

urlpatterns = [

    
    path('',views.index,name = 'index'),
    path("board/<int:article_id>/",views.detail,name='detail'),
    path('create/<int:question_id>/', views.answer_create, name='answer_create'),
]