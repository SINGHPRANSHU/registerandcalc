from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'x'})

def add(request):
    addition =str(int(request.POST['num2'])+int(request.POST['num2']))
    return render(request,'result.html',{'result':request.POST['hidden']+' the result is '+addition})    