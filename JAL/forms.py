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
            'password': request.POST.get('passWord'),
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


class CreateUserAccount:
    def addUserAccount(request):
        get_account_info = AccountDataForm.getAccountInfo(request)
        models.UserAccount.objects.create(
            user_id = get_account_info['email'],
            user_name = get_account_info['email'],
            email = get_account_info['email'],
            password = get_account_info['password'],
            first_name = get_account_info['firstname'],
            last_name = get_account_info['lastname'],
            address = get_account_info['address'],
            street = get_account_info['street'],
            ctiy = get_account_info['city'],
            country = get_account_info['country'],
            code = get_account_info['code'],
        )



