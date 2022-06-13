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
    
    indexApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
    }

    return render(request, 'index.html', indexApi)

def about(request):
    
    indexApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
    }

    return render(request, 'about.html', indexApi)

def detail(request):
    
    indexApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
    }

    return render(request, 'detail.html', indexApi)
    
def products(request):
    
    indexApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('appTitle'),
    }

    return render(request, 'products.html', indexApi)