from django.shortcuts import render

# Create your views here.
from blog import models
from django.shortcuts import HttpResponse
from blog.models import User
from blog import add
import datetime

def db_handle(request):
    models.Demo.objects.create(car_num='陕E-BV886',park_name='中医院', jinru_date='2020-1-1',
    chuqu_date='2022-2-06',time='1')
    user1 = User(company='tuotuo',name='zhang',password='zhang', phone = '11111111', createtime=datetime.datetime.now())
    user1.save()
    return HttpResponse('OK')

def add_user(request):
    if(request.POST):
        add.add_user_post(request)
    return render(request, 'register.html')

def query_user(request):
    if(request.POST):
        query_user = request.POST['user-name']
        user = User.objects.filter(name=query_user).first()
        if(user is not None):
            context={}
            context['name'] = user.name
            context['password'] = user.password
            context['phone'] = user.phone
            context['company'] = user.company
            context['createtime'] = user.createtime
            print(context)
            return render(request, 'user_info.html', context)
        else:
            return HttpResponse('未找到该用户')
        