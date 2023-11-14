from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from urllib import request
import os
import re
from JAL import models
from JAL import urls
from JAL import data_source
from JAL import images
from JAL import forms
from JAL import verify

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse

print('\n>>> this is views.py <<< ')

'''
    Part: user interface

    Part: login module
    login | signUp | verify

    Part: user account module

    Part: order cart module

    Part: manager module
    edit index | edit listing | edit coupon

    Part: check asin
    csv & db

    Part: save data
    
'''

'''
Part: user interface
'''
def _index_(request):
    # '''
    # get cookies
    # '''
    # user_id = request.COOKIES.get('is_login')
    # user_status = request.COOKIES.get('is_login')
    # csrftoken = request.COOKIES.get('csrftoken')
    
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    
    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    '''
    index IMG
    '''
    img_show_dict = {}
    for i in range(len(asin_db_list)):
        img_show_dict[asin_db_list[i]] = os.listdir('static/image/show/' + asin_db_list[i])
        for k in range(len(img_show_dict[asin_db_list[i]])):
            img_show_dict[asin_db_list[i]] = img_show_dict[asin_db_list[i]][k].replace('.jpg', '')

    product_description = models.ProductDescription.objects.all().values()
    
    htmlApi = {
        'page_id': 'index',
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,
        'user_name': user_name,


        'asin_code': asin_db_list,
        'includ_user_id_url': data_source.nav()['_index_']['includ_user_id_url'],
        'product_info': models.Listing.objects.all().values(),
        'product_asin': asin_db_list,
        'img_name': img_show_dict,
        'first_img': models.Listing.objects.filter(status='01',asin='B0BRHWQ27R').values('first_img'),
        'product_title': models.Listing.objects.filter(asin='B0BRHWQ27R').values()[0],
        'product_bullet_point': eval(models.Listing.objects.filter(asin='B0BRHWQ27R').values()[0]['bullet_point']),
        'product_description': product_description,
        # 'csrftoken': csrftoken,

    }
    return render(request, 'index.html', htmlApi)



def _about_(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    htmlApi = {
        'page_id': 'about',
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,
        'user_name': user_name,
    }
    return render(request, 'about.html', htmlApi)
    


def _products_(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    
    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    htmlApi = {
        'page_id': 'products',
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,
        'user_name': user_name,

        # 'includ_user_id_url': data_source.nav()['_index_']['includ_user_id_url'],
        ### get all products info, but status is '00'
        'lenth': len(models.Listing.objects.filter(status='01')),
        'product_info': models.Listing.objects.filter(status='01'),
        'product_image': '',
        'product_title': '',
    }
    return render(request, 'products.html', htmlApi)


def _detail_(request, asin):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    
    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    print('oooooooooo',asin)
    htmlApi = {
        'page_id': asin,
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,
        'user_name': user_name,

        'product_img': detailImg(asin),
        'product_info': models.Listing.objects.filter(asin=asin).values()[0],
        'product_price': models.Listing.objects.filter(asin=asin).values()[0],
        ### the data tpye is 'str' that got from DB
        ### method eval() can changed 'str' to 'list' or 'dict'
        'product_bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
        'product_description': models.Listing.objects.filter(asin=asin).values()[0],
        'sales_status': '',
        'cupon': '',
        'amazon': 'https://www.amazon.com/dp/' + asin,
    }
    return render(request, 'detail.html', htmlApi)





'''
Part: login module
Login | SignUp | Verify
'''
def _login_(request):
    _logout_(request)
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    '''
    verify user_status online
    '''
    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    print(user_status,user_email,user_name)
    htmlApi = {
        'page_id': 'login',
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,
        'user_name': user_name,
        'account_email': {'email':'Email'},
    }
    return render(request, 'login.html', htmlApi)


def _logout_(request):
    # '''
    # del cookies
    # '''
    # rep = redirect('/JAL/login')
    # rep.delete_cookie("is_login")
    # return rep
    '''
    del session
    '''
    # del request.session["key"]
    request.session.flush()
    return redirect('/JAL/login')


def createAccount(request):
    _logout_(request)
    # '''
    # get session
    # '''
    # user_status = request.session.get('user_status')
    # user_email = request.session.get('user_email')
    
    # if not user_status:
    #     user_name = 'Login'
    # else:
    #     user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    if request.method == 'GET':
        htmlApi = {
            'page_id': 'createAccount',
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            # 'user_status': user_status,
            # 'user_account': user_email,
            # 'user_name': user_name,
            'account_email': {'email':'Email'},
            # 'msg': is_valid.errors,

            # 'user_account': verifyUserAccount(request),
        }
        return render(request, 'create-account.html', htmlApi)
    if request.method == 'POST':
        '''
        verify account valid
        '''
        is_valid = forms.AccountDataForm(request.POST)
        if not is_valid.is_valid():
            htmlApi = {
                'page_id': 'createAccount',
                'nav_index': data_source.nav()['_index_'],
                'nav_nav': data_source.nav()['_nav_'],
                'nav_account': data_source.nav()['_account_'],
                # 'user_status': user_status,
                # 'user_account': user_email,
                # 'user_name': user_name,
                'msg': is_valid.errors,

                # 'user_account': verifyUserAccount(request),
            }
            return render(request, 'create-account.html', htmlApi)
    else:
        return HttpResponse('hello world')



@csrf_protect
@csrf_exempt
@requires_csrf_token
def verifyAccountDone(request, action):
    '''
    verify account valid
    '''
    account_form = forms.AccountDataForm(request.POST)
    '''
    account is not valid
    '''
    if action == 'createAccount' and not account_form.is_valid():        
        htmlApi = {
            'page_id': 'createAccount',
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            # 'user_status': user_status,
            # 'user_account': user_email,
            # 'user_name': user_name,
            # 'account_emial': {'email':'Email'},

            'msg': account_form.errors,
            'products': 'products',
        }
        return render(request, 'create-account.html', htmlApi)
    if action == 'login' and not account_form.is_valid():
        print('???',account_form.cleaned_data,account_form.errors)
        
        htmlApi = {
            'page_id': 'login',
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            # 'user_status': user_status,
            # 'user_account': user_email,
            # 'user_name': user_name,
            # 'account_email': {'email':'Email'},

            'msg': account_form.errors,
            'products': 'products',
        }
        return render(request, 'login.html', htmlApi)
    else:
        '''
        account is valid, verify exist
        '''
        verify_user_account = verify.VerifyAccount.verifyEmail(request)
        verify_user_password = verify.VerifyAccount.verifyPassWord(request)

        '''
        account is exist, again
        '''
        if action == 'createAccount' and verify_user_account[0] == True:
            # CreateUserAccount.addUserAccount(request)
            htmlApi = {
                'page_id': 'createAccount',
                'nav_index': data_source.nav()['_index_'],
                'nav_nav': data_source.nav()['_nav_'],
                'nav_account': data_source.nav()['_account_'],
                # 'user_status': user_status,
                # 'user_account': user_email,
                # 'user_name': user_name,

                'tip': verify_user_account[1] + ' is exist',
                'products': 'products',
            }
            return render(request, 'create-account.html', htmlApi)
        '''
        account is not exist, create it
        '''
        if action == 'createAccount' and verify_user_account[0] == False:
            CreateUserAccount.addUserAccount(request)
            '''
            set_session
            '''
            request.session['user_status'] = True
            request.session['user_email'] = verify_user_account[1]

            htmlApi = {
                'nav_index': data_source.nav()['_index_'],
                'nav_nav': data_source.nav()['_nav_'],
                'nav_account': data_source.nav()['_account_'],
                'account_create': True,
                'user_status': True,
                'user_account': verify_user_account[1],
                # 'user_name': verify_user_account[1],
                'user_name': re.findall(r'([a-zA-Z0-9_.+-]+)@', verify_user_account[1])[0],
                
                'tip': verify_user_account[1] + ' is created',
                # 'account_email': account_form.cleaned_data,
                'products': 'products',
                'img': '/static/image/yeah/yeah.jpg'
            }
            return render(request, 'done.html', htmlApi)
        '''
        login success, set session, and redirect to index or other page
        '''
        if action == 'login' and verify_user_password == True:
            # '''
            # # set_cookie
            #     # key : cookie的名称
            #     # value : 保存的cookie的值
            #     # max_age: 保存的时间，以秒为单位
            #     # expires: 过期时间，为datetime对象或时间字符串
            # '''
            # _urls_ = data_source.nav(verify_user_account[1])['_account_']['myAccount'][0]
            # rep = redirect(_urls_)
            # key = 'is_login'
            # value = verify_user_account[1]
            # rep.set_cookie(key, value)
            # return rep

            '''
            set_session
            '''
            # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', verify_user_account[1])[0]
            request.session['user_status'] = True
            request.session['user_email'] = verify_user_account[1]
            # request.session['user_name'] = user_name
            # request.session = {
            #     'user_status': True,
            #     'user_email': verify_user_account[1],
            #     'user_name': user_name,
            # }
            request.session.set_expiry(180)
            _urls_ = data_source.nav()['_account_']['myAccount'][0]
            return redirect(_urls_)
        '''
        account is noe exist, again
        '''
        if action == 'login' and verify_user_account[0] == False:
            # CreateUserAccount.addUserAccount(request)
            htmlApi = {
                'page_id': 'login',
                'nav_index': data_source.nav()['_index_'],
                'nav_nav': data_source.nav()['_nav_'],
                'nav_account': data_source.nav()['_account_'],
                # 'user_status': user_status,
                # 'user_account': user_email,
                # 'user_name': user_name,

                'email_tip': verify_user_account[1] + ' is not exist',
                # 'account_email': account_form.cleaned_data,

                'products': 'products',
            }
            return render(request, 'login.html', htmlApi)
        '''
        password error, again
        '''
        if action == 'login' and verify_user_password == False:
            # CreateUserAccount.addUserAccount(request)
            htmlApi = {
                'page_id': 'login',
                'nav_index': data_source.nav()['_index_'],
                'nav_nav': data_source.nav()['_nav_'],
                'nav_account': data_source.nav()['_account_'],
                # 'user_status': user_status,
                # 'user_account': user_email,
                # 'user_name': user_name,

                'password_tip': 'Password error',
                'account_email': account_form.cleaned_data,

                'products': 'products',
            }
            return render(request, 'login.html', htmlApi)

'''
END: Login SignUp Verify
'''


'''
Part: user account module
'''
def myAccount(request):
    # user_id = '@@'
    # status = request.COOKIES.get('is_login')
    # user_id = request.COOKIES.get('is_login')
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')

    if not user_status:
        user_name = 'Login'
        urls_index = data_source.nav()['_account_']['login'][0]
        rep = redirect(urls_index)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        user_account = models.UserAccount.objects.filter(email=user_email).values()[0]

        htmlApi = {
            'page_id': 'myAccount',

            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_account['user_name'],

            'user_account': user_account,
            
        }

        return render(request, 'my-account.html', htmlApi)


def editAccount(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    
    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    htmlApi = {
        'page_id': 'account',
        'asin_code': asin_db_list,

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,
        'user_name': user_name,

        'user_account': models.UserAccount.objects.filter(email=user_email).values()[0],

    }

    return render(request, 'edit-account.html', htmlApi)


@csrf_protect
@csrf_exempt
@requires_csrf_token
def editAccountDone(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    
    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    htmlApi = {
            'account_edit': True,
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            # 'tag': 'Your acount update  ',
            # 'status': data_source.DataForm.getIndexData(request),
            'status': CreateUserAccount.saveUserAccount(request, user_email),
            'view': data_source.nav()['_index_']['index'],
            'again': data_source.nav()['_admin_']['EditIndex'],
            'img': '/static/image/yeah/yeah.jpg'
        }

    return render(request, 'done.html', htmlApi)


def myCart(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')

    if not user_status:
        urls_index = data_source.nav()['_account_']['login'][0]
        rep = redirect(urls_index)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']
        htmlApi = {
            'page_id': 'myCart',
            'asin_code': asin_db_list,

            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            'product_info': models.Listing.objects.filter(asin='B0BTXB89PG').values()[0],
            'asin': detailImg('B0BTXB89PG'),
            'url_page_id_order': page_id[6],

        }

        return render(request, 'my-cart.html', htmlApi)





'''
Part: order module
'''
@csrf_protect
@csrf_exempt
@requires_csrf_token
def _order_(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')

    if not user_status:
        urls_index = data_source.nav()['_account_']['login'][0]
        rep = redirect(urls_index)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        htmlApi = {
            'page_id': 'order',
            'asin_code': asin_db_list,

            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            'product_info': models.Listing.objects.filter(asin='B0BTXB89PG').values()[0],
            'asin': detailImg('B0BTXB89PG'),
            
        }

        return render(request, 'order.html', htmlApi)



'''
Part: manager module
edit index | edit listing | edit coupon
'''
def _admin_(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)
    
    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'nav_admin': data_source.nav()['_admin_'],
        'user_status': user_status,
        'user_account': True,

        'listing': models.Listing.objects.all().values(),
        'edit_index': 'adminjessie&edit-index',
        'edit_listing': 'adminjessie&edit-listing',
    }

    return render(request, 'admin.html', htmlApi)


def managerProductList(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)

    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'nav_admin': data_source.nav()['_admin_'],
        # 'user_status': user_status,
        'user_account': user_email,
        # 'user_name': user_name[0][0],

        'listing': models.Listing.objects.all().values(),
        'admin': 'adminjessie',

    }

    return render(request, 'manager-product-list.html', htmlApi)


def editIndex(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)

    product_description = models.ProductDescription.objects.all().values()
    
    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'nav_admin': data_source.nav()['_admin_'],
        # 'user_status': user_status,
        'user_account': user_email,
        # 'user_name': user_name[0][0],

        'admin': 'adminjessie',
        'asin': product_description,
        'bullet_point': product_description,
        'id': product_description,
        'tips': 'tips',

    }

    return render(request, 'edit-index.html', htmlApi)

@csrf_protect
@csrf_exempt
@requires_csrf_token
def editIndexDone(request):
    # print(saveIndexData())
    htmlApi = {
            'admin_index': True,
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],

            'tag': 'edit index is   ',
            # 'status': data_source.DataForm.getIndexData(request),
            'status': saveIndexData(request),
            'view': data_source.nav()['_index_']['index'],
            'again': data_source.nav()['_admin_']['EditIndex'],
            'img': '/static/image/yeah/yeah.jpg'
        }

    return render(request, 'done.html', htmlApi)

def editListing(request, asin):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)
    
    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'nav_admin': data_source.nav()['_admin_'],
        # 'user_status': user_status,
        'user_account': user_email,
        # 'user_name': user_name[0][0],

        'asin': asin,
        'listing': models.Listing.objects.filter(asin=asin).values()[0],
        'bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
        'len_bullet_point': len(eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point'])),
        'edit_listing': data_source.nav()['_admin_']['EditListing'],
    }

    return render(request, 'edit-listing.html', htmlApi)


@csrf_protect
@csrf_exempt
@requires_csrf_token
def editListingDone(request, asin):
    htmlApi = {
        'admin_listing': True,
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],

        'tag': 'edit listing done,  ',
        # 'status': data_source.DataForm.editListing(request, asin),
        'status': saveListing(request, asin),
        'view': 'products&asin=' + asin,
        'again': data_source.nav()['_admin_']['EditListing'] + '=' + asin,
        'edit_listing': data_source.nav()['_admin_']['EditListing'],
        'img': '/static/image/yeah/ok.jpg',
    }

    return render(request, 'done.html', htmlApi)





'''
CreateProduct addAsin addListing addFirstImg addSevenImg addAPlusImg
'''
class CreateProduct:
    '''
    from CSV
    '''
    '''
    from From
    '''
    '''
    from Syn
    '''
    def addAsin(asin):
        models.AsinInfo.objects.create(
            asin = asin,
            sku = asin + '-tempName',
            sku_sn = asin + '-tempName-',
        )
    def addListing(asin):
        models.Listing.objects.create(
            asin = asin,
            sku = asin,
            sku_sn = asin,
            title = data_source.DataCSV.listingTitle(asin)['Product Title'],
            price = 39.99,
            bullet_point = data_source.DataCSV.bulletPoint(asin)['Bullet Point'],
            description = data_source.DataCSV.__description__(asin)['Description'],
            first_img = images.Img.firstImg(asin, '7'),
            status = '01',
        )
    def addImgUrl(asin):
        pass



'''
Create UserAccount addAccount addUserInfo addCart addOder
'''
class CreateUserAccount:
    def addUserAccount(request):
        # '''
        # '''
        # email = 'lfeng0309@gmail.com'
        # email_name = r'([a-zA-Z0-9_.+-]+)@'
        # email_plateform = r'([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)'
        # print('rerererererere',re.findall(email_name, email))
        get_account_info = forms.getAccountInfo(request)
        models.UserAccount.objects.create(
            user_id = data_source.generate_random_8_digit(),
            user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', get_account_info['email'])[0],
            email = get_account_info['email'],
            password = get_account_info['password'],
            # first_name = get_account_info['firstname'],
            # last_name = get_account_info['lastname'],
            # address = get_account_info['address'],
            # street = get_account_info['street'],
            # ctiy = get_account_info['city'],
            # country = get_account_info['country'],
            # code = get_account_info['code'],
        )
    '''
    save data after edit account
    '''
    def saveUserAccount(request, user_email):
        get_account_info = forms.getAccountInfo(request)
        try:
            '''
            save the data that has been changed from edit.html to DB
            '''
            db_table_useraccount = models.UserAccount.objects.get(email=user_email)
            db_table_useraccount.user_name = get_account_info['user_name']
            db_table_useraccount.password = get_account_info['password']
            db_table_useraccount.first_name = get_account_info['first_name']
            db_table_useraccount.last_name = get_account_info['last_name']
            db_table_useraccount.address = get_account_info['address']
            db_table_useraccount.street = get_account_info['street']
            db_table_useraccount.city = get_account_info['city']
            db_table_useraccount.country = get_account_info['country']
            db_table_useraccount.code = get_account_info['code']
            db_table_useraccount.save()
            return 'Congratulations!'
        except:
            error = str(user_email) + ' please try again...'
            return error
# db_table_useraccount = models.UserAccount.objects.get(email='lfeng@')
# print('aaaaaaaaaaaaaa',db_table_useraccount.user_name)


'''
Part: save data
check Asin between AsinInfo DB and CSV, if new, update table AsinInfo
'''
asin_csv_list = data_source.DataCSV.asinList()
asin_db_list = data_source.AsinDB.asinList()
print('oooooo from DB, Total:', len(asin_db_list), '\n', asin_db_list, '\n')
if len(asin_csv_list) == len(asin_db_list):
    '''
    the same csv and mySql_db, return None
    '''
    print('oooooo no new asin', '\n')

elif len(asin_csv_list) > len(asin_db_list):
    '''
    more csv, return new asin from csv
    '''
    # new_asin_list = []
    for asin in asin_csv_list:
        if asin in asin_db_list:
            pass
        else:
            # new_asin_list.append(asin)
            CreateProduct.addAsin(asin)
            CreateProduct.addListing(asin)
    print('oooooo have new asin... ', asin, 'saving...', '\n')
    # return new_asin_list

elif len(asin_csv_list) < len(asin_db_list):
    '''
    more mySql_db, delete different asin, and return asin list from mySql DB
    '''
    print('oooooo asin_csv_list less than asin_db_list, Check it!')
else:
    print('oooooo error..., Check Please!')



'''
check Listing from DB, if False, create it
'''
if models.Listing.objects.all():
    print('Table Listing is',True)
else:
    print('Table Listing is',False)
    for asin in asin_db_list:
        CreateProduct.addListing(asin)



'''
save data after edit index
check ProductDescription from DB, if False, create it
'''
def saveIndexData(request):
    get_index_data = forms.getIndexData(request)
    try:
        '''
        save
        '''
        db_table_index = models.ProductDescription.objects.get(id=get_index_data['id'])
        db_table_index.asin = get_index_data['asin']
        db_table_index.bullet_point_01 = get_index_data['bullet_point_01']
        db_table_index.bullet_point_02 = get_index_data['bullet_point_02']
        db_table_index.bullet_point_03 = get_index_data['bullet_point_03']
        db_table_index.url = get_index_data['url']
        db_table_index.save()
        # print('00000000',db_table_index)
        return 'Yeah, Save success!'
    except:
        '''
        if False, create it
        '''
        models.ProductDescription.objects.create(
            id = get_index_data['id'],
            asin = get_index_data['asin'],
            bullet_point_01 = get_index_data['bullet_point_01'],
            bullet_point_02 = get_index_data['bullet_point_02'],
            bullet_point_03 = get_index_data['bullet_point_03'],
            url = get_index_data['url']
        )
        return 'Create it done!'



'''
save data after edit listing
'''
def saveListing(request, asin):
    get_listing_data = forms.getListingData(request, asin)
    try:
        '''
        save the data that has been changed from edit.html to DB
        '''
        db_table_listing = models.Listing.objects.get(asin=asin)
        db_table_listing.title = get_listing_data['title']
        db_table_listing.price = get_listing_data['price']
        db_table_listing.bullet_point = get_listing_data['bullet_point']
        db_table_listing.description = get_listing_data['description']
        db_table_listing.status = get_listing_data['status']
        db_table_listing.save()

        # db_table_productinfo = models.ProductInfo.objects.get(asin=asin)
        # db_table_productinfo.title = get_listing_data['title']
        # db_table_productinfo.price = get_listing_data['price']
        # db_table_productinfo.bullet_point = get_listing_data['bullet_point']
        # db_table_productinfo.description = get_listing_data['description']
        # db_table_productinfo.status = get_listing_data['status']
        # db_table_productinfo.save()

        return 'Congratulations!'
    except:
        error = asin + ' is not in productlist, please try again...'
        return error



'''
Global Variable
'''
page_id = ['index', 'about', 'products', 'myCart', 'login', 'signUp', 'order', 'account', 'myAccount', asin_db_list]
# print('look:>>>>>>',page_id[6])



def detailImg(asin):

    detail_img = {
        'img_7_url': images.urlAsinImg(asin_db_list)[asin]['7'],
        'img_970_url': images.urlAsinImg(asin_db_list)[asin]['970'],
        'img_300_url': images.urlAsinImg(asin_db_list)[asin]['300'],
    }

    return detail_img




# class VerifyAccount:
#     '''
#     get account info from DB
#     '''
#     def accountDB():
#         return models.UserAccount.objects.all().values('email','password')
#     '''
#     get account info from web POST
#     '''
#     def getAccountInfo(request):
#         return forms.getAccountInfo(request)
#     '''
#     verify web POST format
#     '''
#     # def verifyFormat(request):
#     #     if VerifyAccount.getAccountInfo(request)['email'] == 'Email' or VerifyAccount.getAccountInfo(request)['email'] == '':
#     #         return False, 'Input email, please!'
#     #     elif VerifyAccount.getAccountInfo(request)['password'] == 'Password' or VerifyAccount.getAccountInfo(request)['password'] == '':
#     #         return False, 'Input password, please!'
#     #     elif '@' not in VerifyAccount.getAccountInfo(request)['email']:
#     #         return False, 'email error'
#     '''
#     verify email, if exist, return True, if not, return False
#     '''
#     def verifyEmail(request):
#         if VerifyAccount.getAccountInfo(request)['email'] == 'Email' or VerifyAccount.getAccountInfo(request)['email'] == '':
#             return False, 'Input email, please!'
#         elif VerifyAccount.getAccountInfo(request)['password'] == 'Password' or VerifyAccount.getAccountInfo(request)['password'] == '':
#             return False, 'Input password, please!'
#         elif VerifyAccount.getAccountInfo(request)['email'] == 'Email' and VerifyAccount.getAccountInfo(request)['password'] == 'password':
#             return False, 'Enter is not valid'
#         elif VerifyAccount.getAccountInfo(request)['email'] == '' and VerifyAccount.getAccountInfo(request)['password'] == '':
#             return False, 'Enter can not null'
#         elif '@' not in VerifyAccount.getAccountInfo(request)['email']:
#             return False, 'email error'
#         '''
#         check user_account from db, if in, return tips
#         '''
#         for index in range(len(VerifyAccount.accountDB())):
#             if VerifyAccount.getAccountInfo(request)['email'] == VerifyAccount.accountDB()[index]['email']:
#                 return True, VerifyAccount.accountDB()[index]['email'], index
#         '''
#         user not in db, return created
#         '''
#         return False, VerifyAccount.getAccountInfo(request)['email']
#     '''
#     check password by index
#     '''
#     def verifyPassWord(request):
#         if VerifyAccount.verifyEmail(request)[0]:
#             if VerifyAccount.getAccountInfo(request)['password'] == VerifyAccount.accountDB()[VerifyAccount.verifyEmail(request)[2]]['password']:
#                 print('herepassword', VerifyAccount.verifyEmail(request)[2], VerifyAccount.accountDB()[VerifyAccount.verifyEmail(request)[2]])
#                 return True
#             else:
#                 return False


