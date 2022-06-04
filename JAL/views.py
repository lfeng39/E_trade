from django.shortcuts import get_object_or_404, render
# from . import images
# from . import ladyBug
# from django.template.defaulttags import register

# Create your views here.
# @register.filter('list')
# def range(value):
#     return range(value)

def nav(type):
    url = ['about', 'product', 'zmh', 'ydj', 'ddl',]
    appTitle = ['About', 'Product', 'ZMH', 'YDJ', 'DDL',]
    if type == 'url':
        return url
    elif type == 'appTitle':
        return appTitle
    else:
        pass

def index(request):
    

    indexApi = {
        'url': nav('url'),
        'appTitle': nav('appTitle'),

    }

    return render(request, 'index.html', indexApi)