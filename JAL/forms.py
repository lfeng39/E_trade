from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import pandas as pd
import random
import os
from django import forms
from urllib import request
from JAL import models
from JAL import views
from JAL import data_source

'''
Sava user account data into DB
'''
# class AccountDataForm(forms.Form):
class AccountDataForm:
    def getAccountInfo(request):
        # 获取前端数据内容
        get_account_dict = {
            'userid': request.POST.get('email'),
            'usesrname': request.POST.get('email'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'firstname': request.POST.get('email'),
            'lastname': request.POST.get('email'),
            'address': request.POST.get('email'),
            'street': request.POST.get('email'),
            'city': request.POST.get('email'),
            'country': request.POST.get('email'),
            'code': '12345',
        }
        # 保存至UserAccount
        

        return get_account_dict
    
    def accountVerify():
        pass






