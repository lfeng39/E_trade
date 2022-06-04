from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # path('about',views.about, name='about'),
    # path('product',views.product, name='product'),
    # path('zmh',views.zmh, name='zmh'),
    # path('ydj',views.ydj, name='ydj'),
    # path('ddl',views.ddl, name='ddl'),
]