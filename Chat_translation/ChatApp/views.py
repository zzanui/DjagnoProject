from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return HttpRequest("<h1>Hello, world. You're at the polls index.</h1>")
# Create your views here.
