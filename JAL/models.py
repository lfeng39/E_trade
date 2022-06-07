from django.db import models

# Create your models here.
def nav(type):
    
    url = ['about', 'product', 'zmh', 'ydj', 'ddl',]
    appTitle = ['About', 'Product', 'ZMH', 'YDJ', 'DDL',]
    
    nav = {
        'About': 'about',
        'Product': 'product',
        'ZMH': 'zmh',
        'YDJ': 'ydj',
        'DDL': 'ddl',
    }

    if type == 'url':
        return url
    elif type == 'appTitle':
        return appTitle
    elif type == 'nav':
        return nav
    else:
        pass