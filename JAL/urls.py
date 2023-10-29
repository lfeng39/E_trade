from urllib import request
from django.urls import path, re_path
from django.shortcuts import render, HttpResponse, redirect
from JAL import views
from JAL import data_source
from JAL import models

print('\n>>> this is urls.py <<<')

app_name = 'jal'


print('===========================================')
print('===========================================')




urlpatterns = [
    # ex: /polls/
    # url 按顺序查找页面
    path('', views._index_, name=''),
    # path('index', views._index_, name=''),
    path('brand',views._about_, name=''),
    path('products',views._products_, name=''),
    path('products&asin=<asin>',views._detail_, name=''),
    path('login',views._login_, name=''),
    path('signUp',views.signUp, name=''),
    path('cart',views.myCart, name=''),
    path('order',views._order_, name=''),
    path('account',views._account_, name=''),
    path('myAccount',views.myAccount, name=''),
    path('yes=<asin>',views.postData, name=''),
    path('verify',views.userAccount, name=''),
    path('admin&=jessie',views._admin_, name=''),
    path('admin&edit=<asin>',views.editListing, name=''),
    path('admin&=jessie&manager',views.managerProductList, name=''),
    path('admin&editstatus=done=<asin>',views.editListingDone, name=''),
    path('admin&=jessie&editIndex',views.editIndex, name=''),
    path('admin&edit-index-done',views.editIndexDone, name=''),
]