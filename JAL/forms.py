
import pandas as pd
import os
from django import forms
from urllib import request
from JAL import models
from JAL import views
from JAL import data_source

'''
Sava user account data into DB
'''
class AccountDataForm(forms.Form):
    def getAccountInfo(request):
        # 获取前端数据内容
        get_account_dict = {
            'email': request.POST.get('Email'),
            'password': request.POST.get('passWord'),
            'firstname': request.POST.get('firstname'),
            'lastname': request.POST.get('lastname'),
            'address': request.POST.get('address'),
            'street': request.POST.get('street'),
            'city': request.POST.get('city'),
            'country': request.POST.get('country'),
            'code': request.POST.get('code'),
        }
        # 保存至UserAccount
        

        return get_account_dict
    
    def accountVerify():
        pass


class CreateUserAccount:
    def addUserAccount():
        get_account_info = AccountDataForm.getAccountInfo(request)
        models.UserAccount.objects.create(
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
