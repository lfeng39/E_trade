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
    
        'asin': {1:'a', 'name':'b'}
    }

    return render(request, 'detail.html', navApi)
    
def products(request):
    
    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
        'product_title': models.getTitle(),
        'product_img': models.getImgURL(),
    }

    return render(request, 'products.html', navApi)

def zmh(request):

    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
        'asin': 59.97,
        'listing': models.listingCon('B09YLLXKDT'),
        'product_img': models.getImgURL(),
        
    }

    return render(request, 'detail.html', navApi)

def ydj(request):

    navApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
        'asin': 15.99,
        'listing': models.listingCon('B09YLKWBMV'),
        'product_img': models.getImgURL(),
    }

    return render(request, 'detail.html', navApi)