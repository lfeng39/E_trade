from urllib import response
from django.shortcuts import get_object_or_404, render
from . import models
# from . import images
# from . import ladyBug
# from django.template.defaulttags import register

# Create your views here.
# @register.filter('list')
# def range(value):
#     return range(value)


def index(request):
    
    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
    }

    return render(request, 'index.html', navApi)

def about(request):
    
    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
    }

    return render(request, 'about.html', navApi)

def detail(request):

    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
    
        'asin': {1:'a', 'name':{1:'x', 2:'y', 'z':'jessie'}}
    }

    return render(request, 'detail.html', navApi)
    
def products(request):
    '''
    'asin': models.asinInfo('asin')
    asinInfo('asin')返回类型：Dict
    {'firstPic':'url', 'title':'str', 'price':'float'}
    html引用：{{ asin.firstPic }}
    '''


    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
        'product_title': models.getTitle(),
        'product_img': models.getImgURL(),
        'productInfo': models.productInfo(),
    }

    return render(request, 'products.html', navApi)

def zmh(request):
    '''
    'asin': models.listingData('asin')
    listingData('asin')返回类型：Dict
    list: asin.img.i
    str: asin.title
    list: asin.five_point.i
    str: asin.pargram
    list: asin.a_plus.i
    '''

    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
        'asin': models.listingData('B09YLLXKDT'),

    }

    return render(request, 'detail.html', navApi)

def ydj(request):

    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
        'asin': models.listingData('B09YLKWBMV'),
    }

    return render(request, 'detail.html', navApi)