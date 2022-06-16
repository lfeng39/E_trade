from django.urls import path

from JAL import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about',views.about, name='about'),
    path('product',views.products, name='product'),
    path('B09YLLXKDT',views.zmh, name='zmh'),
    path('B09YLKWBMV',views.ydj, name='ydj'),
    path('ddl',views.detail, name='ddl'),
]