from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from urllib import request
import pandas as pd
import csv
import os
import sys
from django import forms
from django.http import HttpResponse
from JAL import images
from JAL import models

print('>>> this is data_source.py <<<')



'''
Get the DATA from DB
'''
class AsinDB:
    '''
    get asin from MySql DB
    type data from DB is <class 'django.db.models.query.QuerySet'>
    return Dict
    '''
    # asin_db = models.AsinInfo.objects.all()

    '''
    from DB table AsinInfo
    return data type <class 'list'>
    '''
    def asinList():
        asin_db_list = []
        for asin_dict in models.AsinInfo.objects.all().values('asin'):
            # print('ooooooo',asin_dict['asin'])
            asin_db_list.append(asin_dict['asin'])

        return asin_db_list
    '''
    check asin between DB table and table, if different, syn them
    coming soon...
    '''
 
        


'''
Get the DATA from CSV
'''
class DataCSV:
    '''
    from CSV
    return data type <class 'list'>
    '''
    def asinList():
        csv_file_list = os.listdir('static/csv/')
        asin_csv_list = []
        for csv_file in csv_file_list:
            file_name, file_type = os.path.splitext(csv_file)
            asin_csv_list.append(file_name)
        
        return asin_csv_list

    '''
    return data type is <class 'pandas.core.frame.DataFrame'>
    '''
    def readCSVData(asin):
        csv_pd = pd.read_csv('static/csv/'+ asin + '.csv', encoding = 'gbk', engine='python')
        
        return csv_pd

    
    '''
    return data type is <class 'dict'>
    '''
    def listingTitle(asin):
        csv_pd = DataCSV.readCSVData(asin)
        product_title = {
            csv_pd.iloc[1,0] : csv_pd.iloc[1,1]
        }

        return product_title

    '''
    return data type is <class 'dict'>
    '''
    def bulletPoint(asin):
        csv_pd = DataCSV.readCSVData(asin)
        '''
        put in bullet_point_list what get bullet_point_txt from csv by csv_pd.iloc[],
        '''
        bullet_point_list = []
        for i in range(2,len(csv_pd)):
            bullet_point = csv_pd.iloc[i,0]
            if 'Bullet Point' in str(bullet_point):
                if type(csv_pd.iloc[i,1]) is float:
                    bullet_point_list.append('bullet_point go...')
                else:
                    bullet_point_list.append(csv_pd.iloc[i,1])
        
        bullet_point = {
            'Bullet Point' : bullet_point_list
        }

        return bullet_point

    '''
    return data type is <class 'dict'>
    '''
    def __description__(asin):
        csv_pd = DataCSV.readCSVData(asin)
        for i in range(2,len(csv_pd)):
            Description = csv_pd.iloc[i,0]
            if 'Description' in str(Description):
                __description__ = {
                    csv_pd.iloc[i,0] : csv_pd.iloc[i,1]
                }

        return __description__



'''
Get the DATA from POST
'''
# class DataForm(forms.Form):
class DataForm:
    pass


    
            

'''
sign up
'''
def getUserInfo(request):
    email = request.POST.get('email')
    pass_word = request.POST.get('passWord')
    
    if email == 'Your Email' or pass_word == '123+ABC+!@#':
        pass
    else:
        '''
        save userinfo
        '''
        models.UserAccount.objects.create(
            email = email,
            password = pass_word,
            # first_name = request.POST.get('FirstName'),
            # last_name = request.POST.get('LastName'),
            # address = request.POST.get('Address'),
            # street = request.POST.get('Street'),
            # ctiy = request.POST.get('City'),
            # country = request.POST.get('Country'),
            # code = request.POST.get('Code'),
        )

        '''
        auth_user DB
        '''
        User.objects.create_user(
            username = email,
            password = pass_word,
        )

    return request.POST.get('email'), request.POST.get('passWord')

    '''
    login
    '''





'''
Start-Mould: Nav
'''
http = 'http://'
# _ip_ = '140.82.22.68'
# _ip_ = '192.168.39.84'
_ip_ = '127.0.0.1'
# csrftoken: Eoa1iSdBOEbaTTdopOt49k05uczyAPvv
# _ip_ = '0.0.0.0'
# csrftoken: T83BR0wnzOOGoGNuSw3mw9kOyQWif8Ns
# _ip_ = '822u770q09.zicp.fun:44088'
_port_ = ':8000'
_app_ = '/JAL/'
base_url = http + _ip_ + _port_ + _app_
# base_url = ''
print('oooooo url_now:', base_url)
def nav():
    nav_dict = {
        '_index_' : 
        {
            'index': base_url + '',
            'includ_user_id_url': '',
        },

        '_nav_' : 
        {
            'Brand': base_url + 'brand',
            'Products': base_url + 'products',
            # 'admin': base_url + 'admin',
        },

        '_account_' : 
        {
            'cart': [base_url + 'cart', 'Cart'],
            'login': [base_url + 'login', 'Login'],
            'createAccount': [base_url + 'createAccount', 'Create Account'],
            'order': [base_url + 'order', 'Order'],
            'account': [base_url + 'account', 'Account'],
            'myAccount': [base_url + 'myAccount', 'MyAccount'],
        },
        '_admin_':
        {
            'Dashboard': base_url + 'admin' + 'jessie',
            'EditIndex': base_url + 'admin' + 'jessie' + '&edit-index',
            'EditListing': base_url + 'admin' + 'jessie' + '&edit-listing',
        },
    }
    return nav_dict

'''
End-Mould: Nav
'''


'''
Create random 8 digits
by secrets module
'''
import secrets

def generate_random_8_digit():
    # 10**8 is mean 10*10*10*10*10*10*10*10
    random_number = secrets.randbelow(10**8)
    # format to str
    random_string = f'{random_number:08}'
    return random_string
# print(generate_random_8_digit())