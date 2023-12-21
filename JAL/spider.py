print('>>> this is spider.py <<<')

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import datetime, time, zoneinfo, pytz
from django.utils import timezone
from urllib import request
import requests
import pandas as pd
import os
from django import forms
from django.http import HttpResponse
from JAL import models





'''
Get the DATA from DB
'''
class AsinDB:
    '''
    get asin from MySql DB
    type data from DB is <class 'django.db.models.query.QuerySet'>
    return Dict
    '''
    asin_db = models.AsinInfo.objects.all().values('asin')

    '''
    from DB table AsinInfo
    return data type <class 'list'>
    '''
    def asinList():
        asin_db_list = []
        for asin_dict in AsinDB.asin_db:
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
Citytime: set timezone
'''
print('\n=== Eastern time zone ========================')
all_timezones = pytz.all_timezones
_format_ = '%Y-%m-%d %H:%M:%S %Z %z'
# _format_ = '%Y%m%d %H:%M:%S'
# _format_ = '%m/%d/%Y %H:%M:%S'
# print(all_timezones)
# current_time
local_time = datetime.datetime.now()
print('| BJS_time', local_time, ' |')
# BJS_time
_shanghai_ = pytz.timezone('Asia/Shanghai')
shanghai_time = datetime.datetime.now(tz=_shanghai_).strftime(_format_)
print('| SHA_time', shanghai_time, ' |')
# LON_time
Greenwich_Mean_Time = timezone.now().strftime(_format_)
print('| UTC_time', Greenwich_Mean_Time, ' |')
_lon_ = pytz.timezone('Europe/London')
lon_time = datetime.datetime.now(tz=_lon_).strftime(_format_)
print('| LON_time', lon_time, ' |')
# NYC_time
_nyc_ = pytz.timezone('America/New_York')
nyc_time = datetime.datetime.now(tz=_nyc_).strftime(_format_)
print('| NYC_time', nyc_time, ' |')
# LAX_time
_lax_ = pytz.timezone('America/Los_Angeles')
lax_time = datetime.datetime.now(tz=_lax_).strftime(_format_)
print('| LAX_time', lax_time, ' |')
print('=== Western time zone ========================\n')

def cityTime(city_timezone):
    city_time = pytz.timezone(city_timezone)
    city_time = datetime.datetime.now(tz=city_time)
    return city_time
time_zone = cityTime('America/Los_Angeles')
print(time_zone)
'''
Weather: AccuWeather API | OpenWeather API
'''
# city = ['Los Angeles', 'New York', 'London', 'Wuhan']
def cityWeather(city):
    lang = ['en', 'zh_cn']
    # for city in city:
    OpenWeather = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&lang=' + lang[0] + '&appid=05c5e335a194653cec7c397f6b82ad34&units=metric'
    response = requests.get(OpenWeather)
    
    if response.status_code == 200:
        data = response.json()
        response_city_data = {
            # 'city': city,
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'pressure': data['main']['pressure'],
            'humidity:': data['main']['humidity']
        }
        # print(city,data)
        # print(city,'>',data['main']['temp'],'>',data['weather'][0]['description'],'>','pressure:',data['main']['pressure'],'>','humidity:',data['main']['humidity'])
    else:
        print("i can't get any info about weather")      
    return response_city_data

# print(cityWeather('shanghai'))
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