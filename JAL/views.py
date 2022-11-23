from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from urllib import request
from JAL import models
from JAL import data_source



def _index_(request):
    
    jasonApi = {
        'asin_code': models._asin_,
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.all().values(),
        'product_asin': models._asin_,
        'img_name': models.img_show_dict,
        'page_id': 'index',
    }

    return render(request, 'index.html', jasonApi)



def _about_(request):
    
    jasonApi = {
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'page_id': 'about',
    }

    return render(request, 'about.html', jasonApi)
    


def _products_(request):

    jasonApi = {
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.all().values(),
        'page_id': 'products',
        'product_image': '',
        'product_title': '',
        
    }

    return render(request, 'products.html', jasonApi)



def _detail_(request, asin_transfer):

    asin = asin_transfer
    jasonApi = {
        'page_id': asin,
        'product_img': models.detailImg(asin),
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.filter(asin=asin_transfer).values()[0],
        'product_description': models.ProductDescription.objects.filter(asin=asin_transfer).values()[0],
        'sales_status': '',
        'cupon': '',
    }

    return render(request, 'detail.html', jasonApi)



def _login_(request):
    
    jasonApi = {
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'page_id': 'login',
    }

    # if request.method == "GET":
    #     # href = request.GET.get('href')
    #     return render(request, 'login.html', jasonApi)

    # elif request.method == "POST":

    #     email = request.POST.get('email')
    #     pass_word = request.POST.get('passWord')

    #     if email == "lfeng" and pass_word == "12820839":

    #         return redirect(models.local_url)
            
    #     else:
            
    #         return render(request, 'login.html', jasonApi)
    if models.verifyAccount(request):

        return redirect(models.local_url)
        # return HttpResponse('true')

    else:
        # return HttpResponse('eroor...')
        return render(request, 'login.html', jasonApi)



def signUp(request):
    
    jasonApi = {
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'page_id': 'signUp',
    }

    return render(request, 'sign-up.html', jasonApi)



def _account_(request):
    
    jasonApi = {
        'page_id': 'account',
        'asin_code': models._asin_,
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'asin': models.detailImg('B09YLLXKDT'),
    }

    return render(request, 'account.html', jasonApi)



def myAccount(request):
    
    jasonApi = {
        'page_id': 'myAccount',
        'asin_code': models._asin_,
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'nav': models.nav(),
        'asin': models.detailImg('B09YLLXKDT'),
    }

    return render(request, 'my-account.html', jasonApi)



def postData(request):

    data_source.DataForm.postAccountInfoSignUp(request)
    # data_source.verifyAccount(request)
    test = models.UserAccount.objects.all().values()

    jasonApi = {
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'yes': 'yes',
        'test': test
    }

    return render(request, 'yes.html', jasonApi)


# def test(request):
#     if data_source.verifyAccount(request):
#         return redirect(models.local_url)
#     else:
#         return HttpResponse('eroor...')


def myCart(request):
    
    jasonApi = {
        'page_id': 'myCart',
        'asin_code': models._asin_,
        # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': models.detailImg('B09YLLXKDT'),
        'url_page_id_order': models.page_id[6],
    }

    return render(request, 'my-cart.html', jasonApi)



def _order_(request):

    jasonApi = {
        'page_id': 'order',
        'asin_code': models._asin_,
            # nav-start
        'nav_index': models.nav()['_index_'],
        'nav_nav': models.nav()['_nav_'],
        'nav_account': models.nav()['_account_'],
        # nav-end
        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': models.detailImg('B09YLLXKDT'),
    }

    return render(request, 'order.html', jasonApi)

