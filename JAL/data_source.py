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



# aaa = models.AsinInfo.objects.all()
# print('testtestestestesetatatast',aaa.values)


'''
Get the DATA from CSV or POST or other
'''
class DataSource():
    
    def connectCsv():
        '''
        获取产品数据CSV文件名及后缀
        '''
        csv_file_list = os.listdir('static/csv/')

        return csv_file_list

    def getAsinCvs(type):
        '''
        获取产品数据CSV文件名,文件名均为asin
        '''
        _asin_ = []
        for i in DataSource.connectCsv():
            file_name, file_type = os.path.splitext(i)
            _asin_.append(file_name)

        if type == 'asin':
            return _asin_
        if type == 'file':
            return DataSource.connectCsv()
    

    def readCSVData(asin):
        '''
        链接CSV
        '''
        data_file = []
        for i in DataSource.getAsinCvs('file'):
            data_file.append('static/csv/' + i)

        data_txt = pd.read_csv(data_file[DataSource.getAsinCvs('asin').index(asin)], encoding = 'gbk', engine='python')
        # data_txt = pd.read_csv('static/csv/'+ asin + '.csv', encoding = 'gbk', engine='python')
        
        return data_txt



class parseCSV():

    '''
    返回最新日期，返回最新日期的列值
    '''
    def dataDate(asin):
        csv_pd = DataSource.readCSVData(asin)
        try:
            _date_ = []
            date_index = {}
            columns = list(csv_pd.columns)

            for i in range(len(columns)):
                date_index[columns[i]] = columns.index(columns[i])

            for date in columns:
                if 'listing' in date.lower():
                    _date_.append(date)
            
            maxmin_index = {
                min(_date_) : columns.index(min(_date_)),
                max(_date_) : columns.index(max(_date_))
            }

            return date_index, maxmin_index

        except:
            return 'no data'
    
    def productTitle(asin):
        csv_pd = DataSource.readCSVData(asin)
        product_title = {}
        product_title[csv_pd.iloc[1,0]] = csv_pd.iloc[1,1]

        return product_title

    '''
    以字典的形式输出5点
    '''
    def bulletPoint(asin):
        csv_pd = DataSource.readCSVData(asin)
        '''
        提取5点，放入temp列表中储存
        '''
        temp = []
        # for i in range(7):
        #     temp.append(csv_pd.iloc[i+2,1])
        for i in range(2,len(csv_pd)):
            bullet_point = csv_pd.iloc[i,0]
            if 'Bullet Point' in bullet_point:
                # print(type(bullet_point))
                temp.append(csv_pd.iloc[i,1])
        
        bullet_point = {
            'Bullet Point' : temp
        }

        return bullet_point

    def __description__(asin):
        csv_pd = DataSource.readCSVData(asin)
        for i in range(2,len(csv_pd)):
            Description = csv_pd.iloc[i,0]
            if 'Description' in Description:
                __description__ = {
                    csv_pd.iloc[i,0] : csv_pd.iloc[i,1]
                }

        return __description__



'''
Get the DATA from POST
'''
# class DataForm(forms.Form):
class DataForm():
    def postAccountInfoSignUp(request):
        
        email = request.POST.get('email')
        pass_word = request.POST.get('passWord')
       
        if email == 'Your Email' or pass_word == '123+ABC+!@#':
            pass
        else:

            '''
            获取前端数据内容
            if request.method == 'POST':            
            保存至UserAccount
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

def test(request):
    cart = request.POST.get('cart')
    print('>>>cart<<<',cart)

