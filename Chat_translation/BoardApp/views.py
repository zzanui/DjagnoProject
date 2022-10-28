import re
from django.shortcuts import render

# Create your views here.
def abc(request):
    return render(request,"abc.html")
def getdata(request):
    return render(request,"getdata.html")
