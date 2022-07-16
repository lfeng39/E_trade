from django.urls import path

from JAL import views
from JAL import models

app_name = 'jal'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about',views.about, name='about'),
    path('product',views.products, name='product'),
    path('B09YLLXKDT',views.zmh, name='zmh'),
    path('B09YLKWBMV',views.ydj, name='ydj'),
    path('B09KG4R3YR',views.ddl, name='ddl'),
    path('passWord',views.test, name='test'),
    path('yes',views.postData, name='test'),
    path('login',views.login, name='login'),
    path('signUp',views.signUp, name='signUp'),
]