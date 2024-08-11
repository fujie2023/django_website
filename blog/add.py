from django.shortcuts import render
from django.views.decorators import csrf
import datetime
from blog.models import User
from django.http import HttpResponse

def add_user_post(request):
    user_company = request.POST['user-company']
    user_name = request.POST['user-name']
    user_password = request.POST['user-password']
    user_phone = request.POST['user-phone']
    user_createtime = datetime.datetime.now()
    new_user = User(company=user_company, name=user_name, password=user_password, phone=user_phone, createtime=user_createtime)
    new_user.save()
    # return HttpResponse('ok')
