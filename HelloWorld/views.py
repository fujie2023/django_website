from django.http import HttpResponse
from django.shortcuts import render
import os,sys
from pathlib import Path

def hello(request):
    print(Path(__file__).resolve().parent.parent)
    return HttpResponse("Hello World!")

def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)

def upload(request):
    
    return HttpResponse('upload')