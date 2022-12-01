from urllib import request
from django.urls import path, re_path
from django.shortcuts import render, HttpResponse, redirect
from JAL import views
from JAL import data_source
from JAL import models



app_name = 'jal'



# def userAccount(request):
#     user_account = list(models.UserAccount.objects.all().values('email'))
#     print(user_account)

#     user_account_post = models.verifyAccount(request)

#     for user_account in user_account:
#     # print(user_account)
#         if user_account_post in user_account.values():
#             # print(list(user_account.values())[0])
#             user_account = list(user_account.values())[0]
#             return user_account
#         # else:
#         #     return None


server_url = '140.82.22.68:8000/JAL'
local_url = '127.0.0.1:8000/JAL'
# local_url = 'http://0.0.0.0:8000/JAL/'
base_url = server_url
# base_url = ''


def nav(request, user_id):

    # user_account_verify = models.verifyAccount(request)
    # get_url = '?'+'username='+ user_account_verify

    # print('yes',user_id)
    if user_id:
        nav_dict = {
            '_index_' : {
                'index': base_url + 'index' + '?user_id=' + user_id,
                'includ_user_id_url':  '?user_id=' + user_id,
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
                'index': base_url + '',
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

about = 'about'


urlpatterns = [
    # ex: /polls/
    # url 按顺序查找页面
    path('', views._index_, name=''),
    path('index', views._index_, name=''),
    path(about,views._about_, name=''),
    path('products',views._products_, name=''),
    path('products/<asin_transfer>',views._detail_, name=''),
    path('login',views._login_, name=''),
    path('signUp',views.signUp, name=''),
    path('cart',views.myCart, name=''),
    path('order',views._order_, name=''),
    path('account',views._account_, name=''),
    path('myAccount',views.myAccount, name=''),
    path('yes',views.postData, name=''),
    path('verify',views.userAccount, name=''),
]