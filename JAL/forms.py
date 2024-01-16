print('\n>>> this is forms.py <<<')

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import pandas as pd
import random
import os
from django import forms
from urllib import request
from JAL import models
from JAL import views

'''
Sava user account data into DB
'''
class AccountDataForm(forms.Form):
    email= forms.EmailField(label='email', required=True, error_messages={'required':'Email can not null'})
    password= forms.CharField(label='password', required=True, min_length=6, error_messages={'min_length':'Least 3 characters','required':'Password can not null'})

'''
createAccount | login | edit userAccount
'''
def getAccountInfo(request):
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
    return get_account_dict


'''
edit index
'''
def getIndexData(request):
    get_content_dict = {
        # 'id' : request.POST.get('id'),
        'promote_type' : request.POST.get('promote_type'),
        'promote_code' : request.POST.get('promote_code'),
        'promote_img' : request.POST.get('promote_img'),
        'promote_url' : request.POST.get('promote_url'),
        'promote_channel': request.POST.get('promote_channel'),
        'bullet_point_01' : request.POST.get('bullet_point_01'),
        'bullet_point_02' : request.POST.get('bullet_point_02'),
        'bullet_point_03' : request.POST.get('bullet_point_03'),
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
        bullet_point.append(request.POST.get('bullet_point_' + str( i + 1 )))
    print(bullet_point)
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


'''
create coupon
'''
def getCouponData(request):
    print('create coupon:::',request.POST.get('asin'))
    get_coupon_dict = {
        'title' : request.POST.get('title'),
        'asin' : request.POST.get('asin'),
        'code' : request.POST.get('code'),
        'cash' : request.POST.get('cash'),
        # 'percentage' : request.POST.get('percentage'),
        # 'start_at' : request.POST.get('start_at'),
        # 'end_at' : request.POST.get('end_at'),
        'status' : request.POST.get('status'),
    }
    return get_coupon_dict


