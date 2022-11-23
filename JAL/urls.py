from urllib import request
from django.urls import path, re_path
from django.shortcuts import render, HttpResponse, redirect
from JAL import views
from JAL import data_source
from JAL import models



# def login(request):  # login函数
#     if request.method == "GET":  # 前端如果是get请求
#         return render(request, 'login.html')  # 返回HTML页面。
#     elif request.method == "POST":  # 前端如果是post请求
#         username = request.POST.get("username")  # 获取POST请求中的username值
#         password = request.POST.get("password")  # 获取密码值
#         if username == "zy" and password == "12345":
#             return redirect("/index/")    #重定向到index页面
#         else:  # 如果用户名或者密码错误，返回登录页面
#             return render(request, "login.html")

# def index(request):  # index函数
#     return render(request, "index.html")

# B0BFHQTG6R == _asin_[0]
# asin = 'B09YLLXKDT'
# ['B0BFHQTG6R', 'B09KG4R3YR', 'B09YLKWBMV', 'B09YLLXKDT']




app_name = 'jal'

urlpatterns = [
    # ex: /polls/
    # url 按顺序查找页面
    path('', views._index_, name=''),
    path('about',views._about_, name=''),
    path('products',views._products_, name=''),
    path('products/<asin_transfer>',views._detail_, name=''),
    path('login',views._login_, name=''),
    path('signUp',views.signUp, name=''),
    path('cart',views.myCart, name=''),
    path('order',views._order_, name=''),
    path('account',views._account_, name=''),
    path('myAccount',views.myAccount, name=''),
    path('yes',views.postData, name=''),
    path('test',models.verifyAccount, name=''),
]