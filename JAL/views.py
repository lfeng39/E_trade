from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from urllib import request
from JAL import models
from JAL import urls
from JAL import data_source



def userAccount(request):

    user_login = {
        'email' : request.POST.get('email'),
        'password' : request.POST.get('passWord'),
    }

    # user = authenticate(request, username = user_login['email'], password = user_login['password'])
    user_account_db = models.UserAccount.objects.all().values('email','password')

    print('user_login:',user_login)

    try:
        for user_account in user_account_db:
            print('user_account_db:',user_account)
            if user_login == user_account:
                print('>>>',user_account, user_account['email'])
                # user_account = list(user_account.values())[0]
                return user_account['email']
            else:
                pass
    except:
        return None



def _index_(request):

    user = request.GET.get('user_id')
    jasonApi = {
        'asin_code': models._asin_,
        # nav-start
        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav(user)['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.all().values(),
        'product_asin': models._asin_,
        'img_name': models.img_show_dict,
        'page_id': 'index',
        'user_account': user,
        # 'user_account': '',
    }
    print('index>>>',type(user),user)

    return render(request, 'index.html', jasonApi)

    

def _about_(request):
    user = request.GET.get('user_id')
    jasonApi = {
        # nav-start
        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav('')['_account_'],
        # nav-end
        'page_id': 'about',
        'user_account': user,
    }

    return render(request, 'about.html', jasonApi)
    


def _products_(request):
    user = request.GET.get('user_id')
    jasonApi = {
        # nav-start
        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav('')['_account_'],
        # nav-end
        'includ_user_id_url': urls.nav(user)['_index_']['includ_user_id_url'],
        # 'includ_user_id_url': '',
        'product_info': models.ProductInfo.objects.all().values(),
        'page_id': 'products',
        'product_image': '',
        'product_title': '',
        'user_account': user,
        
    }

    return render(request, 'products.html', jasonApi)



def _detail_(request, asin_transfer):
    user = request.GET.get('user_id')
    asin = asin_transfer
    jasonApi = {
        'page_id': asin,
        'product_img': models.detailImg(asin),
        # nav-start
        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav('')['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.filter(asin=asin_transfer).values()[0],
        'product_description': models.ProductDescription.objects.filter(asin=asin_transfer).values()[0],
        'sales_status': '',
        'cupon': '',
        'user_account': userAccount(request),
    }

    return render(request, 'detail.html', jasonApi)



def _login_(request):
    
    jasonApi = {
        # nav-start
        'nav_index': urls.nav('')['_index_'],
        'nav_nav': urls.nav('')['_nav_'],
        'nav_account': urls.nav('')['_account_'],
        # nav-end
        'page_id': 'login',
        # 'user_account': user,
    }

    if request.method == 'GET':
        return render(request, 'login.html', jasonApi)
    elif request.method == 'POST':
        user = userAccount(request)
        if user:
            urls_index = urls.nav(user)['_index_']['index']
            return redirect(urls_index)
        else:
            return render(request, 'login.html', jasonApi)




def signUp(request):
    
    jasonApi = {
        # nav-start
        'nav_index': urls.nav('')['_index_'],
        'nav_nav': urls.nav('')['_nav_'],
        'nav_account': urls.nav('')['_account_'],
        # nav-end
        'page_id': 'signUp',
        'user_account': userAccount(request),
    }

    return render(request, 'sign-up.html', jasonApi)



def _account_(request):
    
    jasonApi = {
        'page_id': 'account',
        'asin_code': models._asin_,
        # nav-start
        'nav_index': urls.nav('')['_index_'],
        'nav_nav': urls.nav('')['_nav_'],
        'nav_account': urls.nav('')['_account_'],
        # nav-end
        'asin': models.detailImg('B09YLLXKDT'),
        'user_account': userAccount(request),
    }

    return render(request, 'account.html', jasonApi)



def myAccount(request):

    user = request.GET.get('user_id')
    my_account = models.UserAccount.objects.filter(email=user).values()[0]

    jasonApi = {
        'page_id': 'myAccount',
        # nav-start
        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav('')['_account_'],
        # nav-end
        'user_account': user,
        'my_account': my_account,
    }

    return render(request, 'my-account.html', jasonApi)



def myCart(request):
    
    jasonApi = {
        'page_id': 'myCart',
        'asin_code': models._asin_,
        # nav-start
        'nav_index': urls.nav('')['_index_'],
        'nav_nav': urls.nav('')['_nav_'],
        'nav_account': urls.nav('')['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': models.detailImg('B09YLLXKDT'),
        'url_page_id_order': models.page_id[6],
        'user_account': userAccount(request),
    }

    return render(request, 'my-cart.html', jasonApi)



def _order_(request):

    jasonApi = {
        'page_id': 'order',
        'asin_code': models._asin_,
            # nav-start
        'nav_index': urls.nav(request)['_index_'],
        'nav_nav': urls.nav(request)['_nav_'],
        'nav_account': urls.nav(request)['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': models.detailImg('B09YLLXKDT'),
        'user_account': userAccount(request),
    }

    return render(request, 'order.html', jasonApi)



def postData(request):

    data_source.DataForm.postAccountInfoSignUp(request)
    # data_source.verifyAccount(request)
    test = models.UserAccount.objects.all().values()

    jasonApi = {
        # nav-start
        'nav_index': urls.nav(request)['_index_'],
        'nav_nav': urls.nav(request)['_nav_'],
        'nav_account': urls.nav(request)['_account_'],
        # nav-end
        'yes': 'yes',
        'test': test,
        'user_account': userAccount(request),
    }

    return render(request, 'yes.html', jasonApi)




# 获取cookie 
# print(request.COOKIES.get('Cookie'))

