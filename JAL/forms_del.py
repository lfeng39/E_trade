
import pandas as pd
import os
from django import forms
from JAL import models

'''
SAVE THE DATA INTO DB
'''
class DataForm(forms.Form):
    def getAccountInfo(request):
        
        # 获取前端数据内容
        if request.method == 'POST':
            getEmail = request.POST.get('email')
            getPassWord = request.POST.get('passWord')
            getFirstName = request.POST.get('FirstName')
            getLastName = request.POST.get('LastName')
            getAddress = request.POST.get('Address')
            getStreet = request.POST.get('Street')
            getCity = request.POST.get('City')
            getCountry = request.POST.get('Country')
            getCode = request.POST.get('Code')
            
        # 保存至UserAccount
        models.UserAccount.objects.create(
            email = getEmail,
            password = getPassWord,
            first_name = getFirstName,
            last_name = getLastName,
            address = getAddress,
            street = getStreet,
            ctiy = getCity,
            country = getCountry,
            code = getCode,
        )

        return getEmail, getPassWord
    
    def accountVerify():
        pass


