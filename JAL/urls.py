from urllib import request
from django.urls import path, re_path
from django.shortcuts import render, HttpResponse, redirect
from JAL import views
from JAL import data_source
from JAL import models



app_name = 'jal'

http = 'http://'
_ip_ = '140.82.22.68'
# _ip_ = '192.168.39.84'
# _ip_ = '127.0.0.1'
# _ip_ = '0.0.0.0'
_port_ = ':8000'
_app_ = '/JAL/'
base_url = http + _ip_ + _port_ + _app_
# base_url = ''
print('url_now>>>', base_url)

def nav(user_id):

    if user_id:
        nav_dict = {
            '_index_' : {
                'index': base_url + 'index' + '?user_id=' + user_id,
                'includ_user_id_url': '?user_id=' + user_id,
            },

            '_nav_' : {
                'About': base_url + 'about' + '?user_id=' + user_id,
                'Product': base_url + 'products' + '?user_id=' + user_id,
            },

            '_account_' : {
                'Cart': [base_url + 'cart', 'cart'],
                'Login': [base_url + 'login', 'login'],
                'SignUp': [base_url + 'signUp', 'signUp'],
                'order': [base_url + 'order', 'order'],
                'account': [base_url + 'account', 'account'],
                'myAccount': [base_url + 'myAccount' + '?user_id=' + user_id, 'myAccount'],
            }
        }
    else:
        nav_dict = {
            '_index_' : {
                'index': base_url + 'index',
                'includ_user_id_url': '',
            },

            '_nav_' : {
                'About': base_url + 'about',
                'Product': base_url + 'products',
            },

            '_account_' : {
                'Cart': [base_url + 'cart', 'cart'],
                'Login': [base_url + 'login', 'login'],
                'SignUp': [base_url + 'signUp', 'signUp'],
                'order': [base_url + 'order', 'order'],
                'account': [base_url + 'account', 'account'],
                'myAccount': [base_url + 'myAccount', 'myAccount'],
            }
        }

    return nav_dict



urlpatterns = [
    # ex: /polls/
    # url 按顺序查找页面
    path('', views._index_, name=''),
    path('index', views._index_, name=''),
    path('about',views._about_, name=''),
    path('products',views._products_, name=''),
    path('products/<asin_transfer>',views._detail_, name='asin_code'),
    path('login',views._login_, name=''),
    path('signUp',views.signUp, name=''),
    path('cart',views.myCart, name=''),
    path('order',views._order_, name=''),
    path('account',views._account_, name=''),
    path('myAccount',views.myAccount, name=''),
    path('yes',views.postData, name=''),
    path('verify',views.userAccount, name=''),
]