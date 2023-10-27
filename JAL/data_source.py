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
        提取5点，放入temp列表中储存
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
    '''
    edit listing
    '''
    def editListing(request, asin):
        try:
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

            '''
            save the data that has been changed from edit.html to DB
            '''
            asin_mySql = models.AsinInfo.objects.all()
            # if asin in LatestAsin.asin_mySql_db():
            db_table_listing = models.Listing.objects.get(asin=asin)
            db_table_listing.title = title
            db_table_listing.price = price
            db_table_listing.bullet_point = bullet_point
            db_table_listing.description = description
            db_table_listing.save()

            db_table_productinfo = models.ProductInfo.objects.get(asin=asin)
            db_table_productinfo.title = title
            db_table_productinfo.price = price
            db_table_productinfo.bullet_point = bullet_point
            db_table_productinfo.description = description
            db_table_productinfo.save()

            db_table_Listing_status = models.Listing.objects.get(asin=asin)
            db_table_Listing_status.status = status
            db_table_Listing_status.save()

            db_table_status = models.ProductInfo.objects.get(asin=asin)
            db_table_status.status = status
            db_table_status.save()

            # else:
            #     pass

            return 'Yeah!!! Congratulations on success!!!'
        except:
            error = asin + ' is not in productlist, please try again...'
            return error

    '''
    edit index
    '''
    def editIndex(request):
        id = request.POST.get('id')
        asin = request.POST.get('asin')
        bullet_point_01 = request.POST.get('bullet_point_01')
        bullet_point_02 = request.POST.get('bullet_point_02')


        db_table_index = models.ProductDescription.objects.get(id=id)
        db_table_index.asin = asin
        db_table_index.bullet_point_01 = bullet_point_01
        db_table_index.bullet_point_02 = bullet_point_02
        db_table_index.save()
        # print('00000000',db_table_index)
        return 'Yeah!!! Save success!!!'

    '''
    sign up
    '''
    def postAccountInfoSignUp(request):
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

