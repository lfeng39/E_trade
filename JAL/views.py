from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from urllib import request
import os
from JAL import models
from JAL import urls
from JAL import data_source
from JAL import images
from JAL import forms

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

    Part: order module

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
    user_id = request.GET.get('user_id')
    product_description = models.ProductDescription.objects.all().values()

    '''
    index IMG
    '''
    img_show_dict = {}
    for i in range(len(asin_db_list)):
        img_show_dict[asin_db_list[i]] = os.listdir('static/image/show/' + asin_db_list[i])
        for k in range(len(img_show_dict[asin_db_list[i]])):
            img_show_dict[asin_db_list[i]] = img_show_dict[asin_db_list[i]][k].replace('.jpg', '')

    jasonApi = {
        'asin_code': asin_db_list,

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],
        'user_account': True,

        'includ_user_id_url': data_source.nav(user_id)['_index_']['includ_user_id_url'],
        'product_info': models.Listing.objects.all().values(),
        'product_asin': asin_db_list,
        'img_name': img_show_dict,
        'first_img': models.Listing.objects.filter(status='01',asin='B0BRHWQ27R').values('first_img'),
        'product_title': models.Listing.objects.filter(asin='B0BRHWQ27R').values()[0],
        'product_bullet_point': eval(models.Listing.objects.filter(asin='B0BRHWQ27R').values()[0]['bullet_point']),
        'page_id': 'index',
        'product_description': product_description,
    }
    print('index>>>',type(user_id),user_id)

    return render(request, 'index.html', jasonApi)



def _about_(request):
    user_id = request.GET.get('user_id')
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav('')['_account_'],
        'user_account': True,

        'page_id': 'about',
        'user_account': True,
    }

    return render(request, 'about.html', jasonApi)
    


def _products_(request):
    user_id = request.GET.get('user_id')
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav('')['_account_'],
        'user_account': True,

        'includ_user_id_url': data_source.nav(user_id)['_index_']['includ_user_id_url'],
        # 'includ_user_id_url': '',
        'lenth': len(models.Listing.objects.filter(status='01')),
        ### get all products info, but status is '00'
        'product_info': models.Listing.objects.filter(status='01'),
        'page_id': 'products',
        'product_image': '',
        'product_title': '',
        
        'abc': '%',
    }

    return render(request, 'products.html', jasonApi)


def _detail_(request, asin):
    user_id = request.GET.get('user_id')
    print('oooooooooo',asin)
    jasonApi = {
        'page_id': asin,
        'product_img': detailImg(asin),

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav('')['_account_'],
        # 'user_account': userAccount(request),
        'user_account': True,

        'product_info': models.Listing.objects.filter(asin=asin).values()[0],
        'product_price': models.Listing.objects.filter(asin=asin).values()[0],
        # 'product_img': '/static/image/products/' + asin + '/v1.00/7/00-Listing-01.jpg'
        ### the data tpye is 'str' that got from DB
        ### method eval() can changed 'str' to 'list' or 'dict'
        'product_bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
        'product_description': models.Listing.objects.filter(asin=asin).values()[0],
        'sales_status': '',
        'cupon': '',
        'amazon': 'https://www.amazon.com/dp/' + asin,

        # 'includ_user_id_url': urls.nav(user)['_index_']['includ_user_id_url'],
        # 'product_info': models.ProductInfo.objects.all().values(),
        # 'product_asin': _asin_,
        # 'img_name': img_show_dict,
        # 'page_id': 'index',
        # 'user_account': user,
    }

    return render(request, 'detail.html', jasonApi)





'''
Part: login module
Login | SignUp | Verify
'''
def _login_(request):
    jasonApi = {

        'nav_index': data_source.nav('')['_index_'],
        'nav_nav': data_source.nav('')['_nav_'],
        'nav_account': data_source.nav('')['_account_'],
        'user_account': True,

        'page_id': 'login',
        # 'user_account': user,
    }

    if request.method == 'GET':
        return render(request, 'login.html', jasonApi)
    elif request.method == 'POST':
        user = verifyUserAccount(request)
        if user:
            urls_index = data_source.nav(user)['_index_']['index']
            return redirect(urls_index)
        else:
            return render(request, 'login.html', jasonApi)


def createAccount(request):
    jasonApi = {

        'nav_index': data_source.nav('')['_index_'],
        'nav_nav': data_source.nav('')['_nav_'],
        'nav_account': data_source.nav('')['_account_'],
        'user_account': True,

        'page_id': 'createAccount',
        # 'user_account': verifyUserAccount(request),
    }

    return render(request, 'sign-up.html', jasonApi)



class VerifyAccount:
    user_account_db = models.UserAccount.objects.all().values('email','password')

    def getUserAccountInfo(request):
        account_info = forms.AccountDataForm.getAccountInfo(request)
        user_account_form = {
            'email' : account_info['email'],
            'password' : account_info['password'],
        }
        return account_info

    def verifyUserAccount(request, type):
        
        '''
        get POST info is error, return tips
        '''
        if VerifyAccount.getUserAccountInfo(request).account_info['email'] == 'Email' or VerifyAccount.account_info['email'] == '':
            return False, 'Input email, please!'
        elif VerifyAccount.account_info['password'] == 'Password' or VerifyAccount.account_info['password'] == '':
            return False, 'Input password, please!'
        elif '@' not in VerifyAccount.account_info['email']:
            return False, 'email error'
        '''
        check user_account from db, if in, return tips
        '''
        for index in range(len(VerifyAccount.user_account_db)):
            if VerifyAccount.user_account_form['email'] == VerifyAccount.user_account_db[index]['email']:
                print('here000000', index, VerifyAccount.user_account_db[index])
                return True, VerifyAccount.user_account_db[index]['email']

        '''
        user not in db, return created
        '''
        return False, VerifyAccount.user_account_form['email']

    def verifyPassWord():
        if VerifyAccount.verifyUserAccount()[0]:
            for index in range(len(VerifyAccount.user_account_db)):
                if VerifyAccount.user_account_form['email'] == VerifyAccount.user_account_db[index]['email']:
                    print('here000000', index, VerifyAccount.user_account_db[index])
                    return True, VerifyAccount.user_account_db[index]['email']


# user_account_db = models.UserAccount.objects.all().values('email','password')
# print(len(user_account_db),user_account_db[1])
# user_account_form = {
#     'email' : '@@@',
#     'password' : '123',
# }
# # print(list(user_account_form.values()))
# for aa in range(len(user_account_db)):
#     print(user_account_db[24])



@csrf_protect
@csrf_exempt
@requires_csrf_token
def verifyAccountDone(request, type):
    verify_user_account = verifyUserAccount(request, type)
    if type == 'createAccount' and verify_user_account[0] == True:
        # CreateUserAccount.addUserAccount(request)
        jasonApi = {
            'nav_index': data_source.nav('')['_index_'],
            'nav_nav': data_source.nav('')['_nav_'],
            'nav_account': data_source.nav('')['_account_'],
            'user_account': True,

            'tips': verify_user_account[1] + ' is exist',
            'products': 'products',
        }
        return render(request, 'sign-Up.html', jasonApi)
    if type == 'createAccount' and verify_user_account[0] == False:
        # CreateUserAccount.addUserAccount(request)
        jasonApi = {
            'nav_index': data_source.nav('')['_index_'],
            'nav_nav': data_source.nav('')['_nav_'],
            'nav_account': data_source.nav('')['_account_'],
            'user_account': True,

            'tips': verify_user_account[1] + ' is created',
            'products': 'products',
        }
        return render(request, 'done.html', jasonApi)
    if type == 'login' and verify_user_account[0] == True:
        # CreateUserAccount.addUserAccount(request)
        jasonApi = {
            'nav_index': data_source.nav('')['_index_'],
            'nav_nav': data_source.nav('')['_nav_'],
            'nav_account': data_source.nav('')['_account_'],
            'user_account': True,

            'tips': verify_user_account[1] + ' is success',
            'products': 'products',
        }
        return render(request, 'done.html', jasonApi)
    if type == 'login' and verify_user_account[0] == False:
        # CreateUserAccount.addUserAccount(request)
        jasonApi = {
            'nav_index': data_source.nav('')['_index_'],
            'nav_nav': data_source.nav('')['_nav_'],
            'nav_account': data_source.nav('')['_account_'],
            'user_account': True,

            'tips': verify_user_account[1] + 'is not exist',
            'products': 'products',
        }
        return render(request, 'login.html', jasonApi)
    # else:
        
    #     jasonApi = {
    #         'nav_index': data_source.nav('')['_index_'],
    #         'nav_nav': data_source.nav('')['_nav_'],
    #         'nav_account': data_source.nav('')['_account_'],
    #         'user_account': True,

    #         'tips': verifyUserAccount(request, type)[1],
    #         'products': 'products',
    #     }
    #     return render(request, 'sign-Up.html', jasonApi)
    
    


# class UserLogin():
# def verifyAccount(request):
    
#     user_account_db = UserAccount.objects.all().values('email','password')
#     post_account_info = data_source.DataForm.postAccountInfoLogin(request)

#     if post_account_info in user_account_db:
#         return post_account_info['email']
#     else:
#         return None


# user_account_db = UserAccount.objects.all().values('email')
# print(user_account_db)

# for dict in user_account_db:
#     print(dict)
#     if 'lfeng' in dict.values():
#         print(list(dict.values())[0])
#     else:
#         print('False')
'''
END: Login SignUp Verify
'''





'''
Part: user account module
'''
def _account_(request):
    jasonApi = {
        'page_id': 'account',
        'asin_code': asin_db_list,

        'nav_index': data_source.nav('')['_index_'],
        'nav_nav': data_source.nav('')['_nav_'],
        'nav_account': data_source.nav('')['_account_'],
        'user_account': userAccount(request),

        'asin': detailImg('B09YLLXKDT'),

    }

    return render(request, 'account.html', jasonApi)



def myAccount(request):
    user_id = request.GET.get('user_id')
    # my_account = models.UserAccount.objects.filter(email=user_id).values()[0]

    jasonApi = {
        'page_id': 'myAccount',

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav('')['_account_'],
        'user_account': True,

        'my_account': 'my_account',
    }

    return render(request, 'my-account.html', jasonApi)



def myCart(request):
    jasonApi = {
        'page_id': 'myCart',
        'asin_code': asin_db_list,

        'nav_index': data_source.nav('')['_index_'],
        'nav_nav': data_source.nav('')['_nav_'],
        'nav_account': data_source.nav('')['_account_'],
        'user_account': userAccount(request),

        'product_info': models.Listing.objects.filter(asin='B0BTXB89PG').values()[0],
        'asin': detailImg('B0BTXB89PG'),
        'url_page_id_order': page_id[6],

    }

    return render(request, 'my-cart.html', jasonApi)





'''
Part: order module
'''
@csrf_protect
@csrf_exempt
@requires_csrf_token
def _order_(request):
    user_id = request.GET.get('user_id')
    jasonApi = {
        'page_id': 'order',
        'asin_code': asin_db_list,

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],
        'user_account': True,

        'product_info': models.Listing.objects.filter(asin='B0BTXB89PG').values()[0],
        'asin': detailImg('B0BTXB89PG'),
        
    }

    return render(request, 'order.html', jasonApi)



def upData(request):
    jasonApi = {
        'page_id': 'upData',

        'nav_index': data_source.nav(request)['_index_'],
        'nav_nav': data_source.nav(request)['_nav_'],
        'nav_account': data_source.nav(request)['_account_'],
        'user_account': userAccount(request),


        'product_info': models.Listing.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': detailImg('B09YLLXKDT'),

    }

    return render(request, 'order.html', jasonApi)





'''
Part: manager module
edit index | edit listing | edit coupon
'''
def _admin_(request):
    user_id = request.GET.get('user_id')
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],
        'nav_admin': data_source.nav('')['_admin_'],
        'user_account': True,

        'listing': models.Listing.objects.all().values(),
        'edit_listing': 'admin&user_id=jessie&editlisting',
        'edit_index': 'admin&user_id=jessie&editIndex',

    }

    return render(request, 'admin.html', jasonApi)


def managerProductList(request):
    user_id = request.GET.get('user_id')
    # asin = asin_transfer
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],
        'nav_admin': data_source.nav('')['_admin_'],
        'user_account': True,

        'listing': models.Listing.objects.all().values(),
        'admin': 'adminjessie',

    }

    return render(request, 'manager-product-list.html', jasonApi)


def editIndex(request):
    user_id = request.GET.get('user_id')
    product_description = models.ProductDescription.objects.all().values()
    
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],
        'nav_admin': data_source.nav('')['_admin_'],
        'user_account': True,

        'admin': 'adminjessie',
        'asin': product_description,
        'bullet_point': product_description,
        'id': product_description,
        'tips': 'tips',

    }

    return render(request, 'edit-index.html', jasonApi)

@csrf_protect
@csrf_exempt
@requires_csrf_token
def editIndexDone(request):
    # print(saveIndexData())
    jasonApi = {

            # 'nav_index': data_source.nav(request)['_index_'],
            # 'nav_nav': data_source.nav(request)['_nav_'],
            # 'nav_account': data_source.nav(request)['_account_'],
            

            'tag': 'edit index is   ',
            # 'status': data_source.DataForm.getIndexData(request),
            'status': saveIndexData(request),
            'again': 'admin&=jessie&editIndex',
            'admin': 'admin&=jessie&editIndex',
            'img': '/static/image/yeah/yeah.jpg'
        }

    return render(request, 'done.html', jasonApi)

def editListing(request, asin):
    user_id = request.GET.get('user_id')
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],
        'nav_admin': data_source.nav('')['_admin_'],
        'user_account': True,

        'asin': asin,
        'listing': models.Listing.objects.filter(asin=asin).values()[0],
        'bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
        'len_bullet_point': len(eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point'])),
        'edit_listing': 'admin&user_id=jessie&editlisting',
    }

    return render(request, 'edit-listing.html', jasonApi)

@csrf_protect
@csrf_exempt
@requires_csrf_token
def editListingDone(request, asin):
    jasonApi = {

        # 'nav_index': data_source.nav(request)['_index_'],
        # 'nav_nav': data_source.nav(request)['_nav_'],
        # 'nav_account': data_source.nav(request)['_account_'],

        'tag': 'edit listing is   ',
        # 'status': data_source.DataForm.editListing(request, asin),
        'status': saveListing(request, asin),
        'view': 'products&asin=' + asin,
        'again': 'admin&edit=' + asin,
        'admin': 'admin&user_id=jessie&editlisting',
        'img': '/static/image/yeah/ok.jpg',
    }

    return render(request, 'done.html', jasonApi)





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
        get_account_info = forms.AccountDataForm.getAccountInfo(request)
        models.UserAccount.objects.create(
            user_id = get_account_info['email'],
            user_name = get_account_info['email'],
            email = get_account_info['email'],
            password = get_account_info['password'],
            first_name = get_account_info['firstname'],
            last_name = get_account_info['lastname'],
            address = get_account_info['address'],
            street = get_account_info['street'],
            ctiy = get_account_info['city'],
            country = get_account_info['country'],
            code = get_account_info['code'],
        )




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
    get_index_data = data_source.DataForm.getIndexData(request)
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
    get_listing_data = data_source.DataForm.getListingData(request, asin)
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

        db_table_productinfo = models.ProductInfo.objects.get(asin=asin)
        db_table_productinfo.title = get_listing_data['title']
        db_table_productinfo.price = get_listing_data['price']
        db_table_productinfo.bullet_point = get_listing_data['bullet_point']
        db_table_productinfo.description = get_listing_data['description']
        db_table_productinfo.status = get_listing_data['status']
        db_table_productinfo.save()

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







