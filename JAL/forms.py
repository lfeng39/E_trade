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
# class AccountDataForm:
'''
createAccount | login | edit userAccount
'''
def getAccountInfo(request):
    # 获取前端数据内容
    get_account_dict = {
        # 'userid': request.POST.get('email'),
        'user_name': request.POST.get('user_name'),
        'email': request.POST.get('email'),
        'password': request.POST.get('password'),
        'first_name': request.POST.get('first_name'),
        'last_name': request.POST.get('last_name'),
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
'''
edit userAccount
'''
# def getUserAccountData(request):
#     # pass
#     user_name = request.POST.get('user_name')
#     password = request.POST.get('password')
#     first_name = request.POST.get('first_name')
#     last_name = request.POST.get('last_name')
#     address = request.POST.get('address')
#     street = request.POST.get('street')
#     ctiy = request.POST.get('ctiy')
#     country = request.POST.get('country')
#     code = request.POST.get('code')


'''
edit index
'''
def getIndexData(request):
    get_content_dict = {
        'id' : request.POST.get('id'),
        'asin' : request.POST.get('asin'),
        'bullet_point_01' : request.POST.get('bullet_point_01'),
        'bullet_point_02' : request.POST.get('bullet_point_02'),
        'bullet_point_03' : '',
        'url' : [],
    }

    return get_content_dict


'''
edit listing
'''
def getListingData(request, asin):
# def editListing(request, asin):
    '''
    get title from edit.html
    '''
    title = request.POST.get('title')

    '''
    get price from edit.html
    '''
    price = request.POST.get('price')

    '''
    get bullepoint from edit.html
    '''
    count = len(eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']))
    bullet_point = []
    for i in range(count):
        bullet_point.append(request.POST.get('bullet_point_'+str(i+1)))
    
    '''
    get description from edit.html
    '''
    description = request.POST.get('description')

    '''
    status
    '''
    status = request.POST.get('status')

    get_listing_data = {
        'title': title,
        'price': price,
        'bullet_point': bullet_point,
        'description': description,
        'status': status
    }

    return get_listing_data




