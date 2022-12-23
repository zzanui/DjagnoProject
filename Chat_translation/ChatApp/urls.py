from django.urls import path

from . import views

app_name = "ChatApp"

urlpatterns = [
    path("api/<int:user_id>/",views.create_room ,name="create_room"),
    path("<str:room_name>/",views.view_room,name="view_room"),
]