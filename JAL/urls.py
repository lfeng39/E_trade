print('\n>>> this is urls.py <<<')

from urllib import request
from django.urls import path, re_path
from django.shortcuts import render, HttpResponse, redirect
# from session import views as session_views
from JAL import views
from JAL import models



app_name = 'jal'


print('===========================================')
print('===========================================')




urlpatterns = [
    # ex: /polls/
    # url 按顺序查找页面
    path('', views.Promote._index_, name=''),
    path('index', views.Promote._index_, name=''),
    path('brand',views.Brand._about_, name=''),
    path('products',views.Product._shelf_, name=''),
    path('products&asin=<asin>',views.Product._listing_, name=''),
    

    path('login',views._login_, name=''),
    path('logout',views._logout_, name=''),
    path('account=login',views.verifyAccountDone, name=''),
    path('createAccount',views.createAccount, name=''),
    path('account=createAccount',views.createAccount, name=''),
    path('cart',views.myCart, name=''),
    path('order',views._order_, name=''),
    path('account',views.myAccount, name=''),
    path('myAccount&=edit',views.editAccount, name=''),
    path('myAccount&=edit-done',views.editAccount, name=''),


    path('adminjessie',views._admin_, name=''),
    path('adminjessie&promote',views.Promote.managePromote, name=''),
    path('adminjessie&promote=create',views.Promote.createPromote, name=''),
    path('adminjessie&promote=create-done',views.Promote.createPromote, name=''),
    path('adminjessie&promote=<code>-edit',views.Promote.editPromote, name=''),
    path('adminjessie&promote=<code>-edit-done',views.Promote.editPromote, name=''),

    path('adminjessie&listing',views.Product.manageListing, name=''),
    path('adminjessie&listing=<asin>-edit',views.Product.editListing, name=''),
    path('adminjessie&listing=<asin>-edit-done',views.Product.editListing, name=''),

    path('adminjessie&coupon', views.Promote._coupon_, name=''),
    path('adminjessie&coupon=create', views.Promote.createCoupon, name=''),
    path('adminjessie&coupon=create-done', views.Promote.createCoupon, name=''),
    path('test', views.test, name=''),


    path('html-msg',views.htmlMsg, name=''),
]