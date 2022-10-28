from django.urls import path
from . import views

urlpatterns = [
    path('',views.abc),
    path('getdata/',views.getdata),
]