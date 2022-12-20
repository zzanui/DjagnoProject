from django.urls import path

from . import views

app_name = "ChatApp"

urlpatterns = [
    path("", views.mainpage,name="mainpage"),
    path("<str:room_name>/",views.room,name="room"),
]