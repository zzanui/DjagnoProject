from django.urls import path

from . import views

urlpatterns = [
    path("mainpage/", views.mainpage,name="mainpage"),
    path("<str:room_name>/",views.room,name="room"),
    path("test/",views.test),
]