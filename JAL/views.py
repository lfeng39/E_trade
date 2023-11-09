from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from urllib import request
import os
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
    print('index>>>', type(user_email), user_email)
    return render(request, 'index.html', htmlApi)



def _about_(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    htmlApi = {
        'page_id': 'about',
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,
    }
    return render(request, 'about.html', htmlApi)
    


def _products_(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    htmlApi = {
        'page_id': 'products',
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,

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

    print('oooooooooo',asin)
    htmlApi = {
        'page_id': asin,
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,

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
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    htmlApi = {
        'page_id': 'login',
        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,
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
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'user_status': user_status,
        'user_account': user_email,

        'page_id': 'createAccount',
        # 'user_account': verifyUserAccount(request),
    }
    return render(request, 'create-account.html', htmlApi)



class VerifyAccount:
    user_account_db = models.UserAccount.objects.all().values('email','password')
    def account_info(request):
        return forms.AccountDataForm.getAccountInfo(request)

    def verifyEmail(request):
        '''
        get POST info is error, return tips
        '''
        if VerifyAccount.account_info(request)['email'] == 'Email' or VerifyAccount.account_info(request)['email'] == '':
            return False, 'Input email, please!'
        elif VerifyAccount.account_info(request)['password'] == 'Password' or VerifyAccount.account_info(request)['password'] == '':
            return False, 'Input password, please!'
        elif '@' not in VerifyAccount.account_info(request)['email']:
            return False, 'email error'
        '''
        check user_account from db, if in, return tips
        '''
        for index in range(len(VerifyAccount.user_account_db)):
            if VerifyAccount.account_info(request)['email'] == VerifyAccount.user_account_db[index]['email']:
                print('here000000', index, VerifyAccount.user_account_db[index])
                return True, VerifyAccount.user_account_db[index]['email'], index
        '''
        user not in db, return created
        '''
        return False, VerifyAccount.account_info(request)['email']
    '''
    check password by index
    '''
    def verifyPassWord(request):
        if VerifyAccount.verifyEmail(request)[0]:
            if VerifyAccount.account_info(request)['password'] == VerifyAccount.user_account_db[VerifyAccount.verifyEmail(request)[2]]['password']:
                print('herepassword', VerifyAccount.verifyEmail(request)[2], VerifyAccount.user_account_db[VerifyAccount.verifyEmail(request)[2]])
                return True
            else:
                return False

# print(data_source.nav('test')['_account_']['myAccount'][0])

@csrf_protect
@csrf_exempt
@requires_csrf_token
def verifyAccountDone(request, type):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    verify_user_account = VerifyAccount.verifyEmail(request)
    verify_user_password = VerifyAccount.verifyPassWord(request)
    if type == 'createAccount' and verify_user_account[0] == True:
        # CreateUserAccount.addUserAccount(request)
        htmlApi = {
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,

            'tips': verify_user_account[1] + ' is exist',
            'products': 'products',
        }
        return render(request, 'create-account.html', htmlApi)
    
    if type == 'createAccount' and verify_user_account[0] == False:
        CreateUserAccount.addUserAccount(request)
        htmlApi = {
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,

            'tips': verify_user_account[1] + ' is created',
            'products': 'products',
        }
        return render(request, 'done.html', htmlApi)
    
    if type == 'login' and verify_user_password == True:
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
        request.session['user_status'] = True
        request.session['user_email'] = verify_user_account[1]
        _urls_ = data_source.nav()['_account_']['myAccount'][0]
        return redirect(_urls_)
    
    if type == 'login' and verify_user_account[0] == False:
        # CreateUserAccount.addUserAccount(request)
        htmlApi = {
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,

            'tips': verify_user_account[1] + ' is not exist',
            'products': 'products',
        }
        return render(request, 'login.html', htmlApi)
    
    if type == 'login' and verify_user_password == False:
        # CreateUserAccount.addUserAccount(request)
        htmlApi = {
            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,

            'tips': 'Password error',
            'products': 'products',
        }
        return render(request, 'login.html', htmlApi)

'''
END: Login SignUp Verify
'''





'''
Part: user account module
'''
def _account_(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    if not user_status:
        urls_index = data_source.nav()['_account_']['login'][0]
        rep = redirect(urls_index)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        htmlApi = {
            'page_id': 'account',
            'asin_code': asin_db_list,

            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,

            'asin': detailImg('B09YLLXKDT'),

        }

        return render(request, 'account.html', htmlApi)



def myAccount(request):
    # user_id = '@@'
    # status = request.COOKIES.get('is_login')
    # user_id = request.COOKIES.get('is_login')
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    # my_account = models.UserAccount.objects.filter(email=user_id).values()[0]

    if not user_status:
        urls_index = data_source.nav()['_account_']['login'][0]
        rep = redirect(urls_index)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        htmlApi = {
            'page_id': 'myAccount',

            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,

            'my_account': models.UserAccount.objects.filter(email=user_email).values()[0],
            
        }

        return render(request, 'my-account.html', htmlApi)


def myCart(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')

    if not user_status:
        urls_index = data_source.nav()['_account_']['login'][0]
        rep = redirect(urls_index)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        htmlApi = {
            'page_id': 'myCart',
            'asin_code': asin_db_list,

            'nav_index': data_source.nav()['_index_'],
            'nav_nav': data_source.nav()['_nav_'],
            'nav_account': data_source.nav()['_account_'],
            'user_status': user_status,
            'user_account': user_email,

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
    
    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'nav_admin': data_source.nav()['_admin_'],
        'user_status': user_status,
        'user_account': user_email,

        'listing': models.Listing.objects.all().values(),
        'edit_listing': 'admin&user_id=jessie&editlisting',
        'edit_index': 'admin&user_id=jessie&editIndex',

    }

    return render(request, 'admin.html', htmlApi)


def managerProductList(request):
    user_email = request.GET.get('user_id')
    # asin = asin_transfer
    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'nav_admin': data_source.nav()['_admin_'],
        # 'user_status': user_status,
        'user_account': user_email,

        'listing': models.Listing.objects.all().values(),
        'admin': 'adminjessie',

    }

    return render(request, 'manager-product-list.html', htmlApi)


def editIndex(request):
    user_email = request.GET.get('user_id')
    product_description = models.ProductDescription.objects.all().values()
    
    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'nav_admin': data_source.nav()['_admin_'],
        # 'user_status': user_status,
        'user_account': user_email,

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

    return render(request, 'done.html', htmlApi)

def editListing(request, asin):
    user_email = request.GET.get('user_id')
    htmlApi = {

        'nav_index': data_source.nav()['_index_'],
        'nav_nav': data_source.nav()['_nav_'],
        'nav_account': data_source.nav()['_account_'],
        'nav_admin': data_source.nav()['_admin_'],
        # 'user_status': user_status,
        'user_account': user_email,

        'asin': asin,
        'listing': models.Listing.objects.filter(asin=asin).values()[0],
        'bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
        'len_bullet_point': len(eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point'])),
        'edit_listing': 'admin&user_id=jessie&editlisting',
    }

    return render(request, 'edit-listing.html', htmlApi)

@csrf_protect
@csrf_exempt
@requires_csrf_token
def editListingDone(request, asin):
    htmlApi = {

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







