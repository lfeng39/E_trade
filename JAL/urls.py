from urllib import request
from django.urls import path, re_path
from django.shortcuts import render, HttpResponse, redirect
# from session import views as session_views
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
    path('index', views._index_, name=''),
    path('brand',views._about_, name=''),
    path('products',views._products_, name=''),
    path('products&asin=<asin>',views._detail_, name=''),
    path('login',views._login_, name=''),
    path('logout',views._logout_, name=''),
    path('createAccount',views.createAccount, name=''),
    path('account=<action>',views.verifyAccountDone, name=''),
    path('cart',views.myCart, name=''),
    path('order',views._order_, name=''),
    path('myAccount',views.myAccount, name=''),
    path('myAccount&=edit',views.editAccount, name=''),
    path('myAccount&=edit-status-done',views.editAccountDone, name=''),
    path('adminjessie',views._admin_, name=''),
    path('adminjessie&edit-index',views.editIndex, name=''),
    path('adminjessie&edit-index-status-done',views.editIndexDone, name=''),
    path('adminjessie&edit-listing',views.managerProductList, name=''),
    path('adminjessie&edit-listing=<asin>',views.editListing, name=''),
    path('adminjessie&edit-listing-status=done=<asin>',views.editListingDone, name=''),

]