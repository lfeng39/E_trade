import email
from urllib import response
from django.shortcuts import get_object_or_404, render
from JAL import models
from JAL import forms
from JAL import styles



def index(request):
    
    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
        'imgShow': models.img_shower,
        'styles': styles.bgContainer(),
        'aaa': styles.position(),
    }

    return render(request, 'index.html', jasonApi)

def login(request):
    
    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
    }

    return render(request, 'login.html', jasonApi)

def signUp(request):
    
    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
    }

    return render(request, 'sign-up.html', jasonApi)

def about(request):
    
    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
    }

    return render(request, 'about.html', jasonApi)

def detail(request):

    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
        'asin': {1:'a', 'name':{1:'x', 2:'y', 'z':'jessie'}}
    }

    return render(request, 'detail.html', jasonApi)
    
def products(request):
    '''
    'asin': models.productInfo()
    productInfo()返回类型：Dict、复合型
    {'img':'url', 'title':'str', 'price':'float'}
    html引用：{{ productInfo.asin.img }}
    '''
    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
        'productInfo': models.productInfo(),
    }

    return render(request, 'products.html', jasonApi)

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

    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
        'asin': models.listingData('B09YLLXKDT')[0],

    }
    
    return render(request, 'detail.html', jasonApi)

def ydj(request):

    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
        'asin': models.listingData('B09YLKWBMV')[0],
    }

    return render(request, 'detail.html', jasonApi)

def ddl(request):

    jasonApi = {
        'url': models.nav('url'),
        'appTitle': models.nav('app_title'),
        'nav': models.nav('nav'),
        'asin': models.listingData('B09KG4R3YR')[0],
    }

    return render(request, 'detail.html', jasonApi)




def test(request):
    
    jasonApi = {
            'url': models.nav('url'),
            'appTitle': models.nav('app_title'),

            'test': forms.DataForm.getData(request)
        }

    return render(request, 'detail.html', jasonApi)


def postData(request):
    # models.saveData(request)
    forms.DataForm.getAccountInfo(request)
    # test = get_object_or_404(models.UserAccount, email = 'jessie@gmail.com')
    test = models.UserAccount.objects.all().values()

    jasonApi = {
            'url': models.nav('url'),
            'appTitle': models.nav('app_title'),
            'nav': models.nav('nav'),
            'yes': 'yes',
            'test': test
        }

    return render(request, 'yes.html', jasonApi)