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

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse

print('\n>>> this is views.py <<< ')

# def _nav_():

data_source.nav('')['_nav_']

def _index_(request):
    user = request.GET.get('user_id')
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

        'nav_index': data_source.nav(user)['_index_'],
        'nav_nav': data_source.nav(user)['_nav_'],
        'nav_account': data_source.nav(user)['_account_'],

        'includ_user_id_url': data_source.nav(user)['_index_']['includ_user_id_url'],
        'product_info': models.Listing.objects.all().values(),
        'product_asin': asin_db_list,
        'img_name': img_show_dict,
        'first_img': models.Listing.objects.filter(status='01',asin='B0BRHWQ27R').values('first_img'),
        'product_title': models.Listing.objects.filter(asin='B0BRHWQ27R').values()[0],
        'product_bullet_point': eval(models.Listing.objects.filter(asin='B0BRHWQ27R').values()[0]['bullet_point']),
        'page_id': 'index',
        'user_account': user,
        'product_description': product_description,
    }
    print('index>>>',type(user),user)

    return render(request, 'index.html', jasonApi)



def _about_(request):
    user = request.GET.get('user_id')
    jasonApi = {

        'nav_index': data_source.nav(user)['_index_'],
        'nav_nav': data_source.nav(user)['_nav_'],
        'nav_account': data_source.nav('')['_account_'],

        'page_id': 'about',
        'user_account': user,
    }

    return render(request, 'about.html', jasonApi)
    


def _products_(request):
    user = request.GET.get('user_id')
    jasonApi = {

        'nav_index': data_source.nav(user)['_index_'],
        'nav_nav': data_source.nav(user)['_nav_'],
        'nav_account': data_source.nav('')['_account_'],

        'includ_user_id_url': data_source.nav(user)['_index_']['includ_user_id_url'],
        # 'includ_user_id_url': '',
        'lenth': len(models.Listing.objects.filter(status='01')),
        ### get all products info, but status is '00'
        'product_info': models.Listing.objects.filter(status='01'),
        'page_id': 'products',
        'product_image': '',
        'product_title': '',
        'user_account': user,
        'abc': '%',
    }

    return render(request, 'products.html', jasonApi)


def _detail_(request, asin):
    user = request.GET.get('user_id')
    print('oooooooooo',asin)
    jasonApi = {
        'page_id': asin,
        'product_img': detailImg(asin),

        'nav_index': data_source.nav(user)['_index_'],
        'nav_nav': data_source.nav(user)['_nav_'],
        'nav_account': data_source.nav('')['_account_'],

        'product_info': models.Listing.objects.filter(asin=asin).values()[0],
        'product_price': models.Listing.objects.filter(asin=asin).values()[0],
        # 'product_img': '/static/image/products/' + asin + '/v1.00/7/00-Listing-01.jpg'
        ### the data tpye is 'str' that got from DB
        ### method eval() can changed 'str' to 'list' or 'dict'
        'product_bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
        'product_description': models.Listing.objects.filter(asin=asin).values()[0],
        'sales_status': '',
        'cupon': '',
        'user_account': userAccount(request),
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
START---Moulde: Login | SignUp | Verify
'''
def _login_(request):
    jasonApi = {

        'nav_index': data_source.nav('')['_index_'],
        'nav_nav': data_source.nav('')['_nav_'],
        'nav_account': data_source.nav('')['_account_'],

        'page_id': 'login',
        # 'user_account': user,
    }

    if request.method == 'GET':
        return render(request, 'login.html', jasonApi)
    elif request.method == 'POST':
        user = userAccount(request)
        if user:
            urls_index = data_source.nav(user)['_index_']['index']
            return redirect(urls_index)
        else:
            return render(request, 'login.html', jasonApi)


def signUp(request):
    jasonApi = {

        'nav_index': data_source.nav('')['_index_'],
        'nav_nav': data_source.nav('')['_nav_'],
        'nav_account': data_source.nav('')['_account_'],

        'page_id': 'signUp',
        'user_account': userAccount(request),
    }

    return render(request, 'sign-up.html', jasonApi)


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
END---Moulde: Login SignUp Verify
'''


def _account_(request):
    jasonApi = {
        'page_id': 'account',
        'asin_code': asin_db_list,

        'nav_index': data_source.nav('')['_index_'],
        'nav_nav': data_source.nav('')['_nav_'],
        'nav_account': data_source.nav('')['_account_'],

        'asin': detailImg('B09YLLXKDT'),
        'user_account': userAccount(request),
    }

    return render(request, 'account.html', jasonApi)



def myAccount(request):
    user_id = request.GET.get('user_id')
    my_account = models.UserAccount.objects.filter(email=user_id).values()[0]

    jasonApi = {
        'page_id': 'myAccount',

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav('')['_account_'],

        'user_account': user_id,
        'my_account': my_account,
    }

    return render(request, 'my-account.html', jasonApi)



def myCart(request):
    jasonApi = {
        'page_id': 'myCart',
        'asin_code': asin_db_list,

        'nav_index': data_source.nav('')['_index_'],
        'nav_nav': data_source.nav('')['_nav_'],
        'nav_account': data_source.nav('')['_account_'],

        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': detailImg('B09YLLXKDT'),
        'url_page_id_order': page_id[6],
        'user_account': userAccount(request),
    }

    return render(request, 'my-cart.html', jasonApi)



def _order_(request):
    jasonApi = {
        'page_id': 'order',
        'asin_code': asin_db_list,

        'nav_index': data_source.nav(request)['_index_'],
        'nav_nav': data_source.nav(request)['_nav_'],
        'nav_account': data_source.nav(request)['_account_'],

        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': detailImg('B09YLLXKDT'),
        'user_account': userAccount(request),
    }

    return render(request, 'order.html', jasonApi)



def postData(request, asin):
    # data_source.DataForm.postAccountInfoSignUp(request)
    # data_source.verifyAccount(request)
    # test = models.UserAccount.objects.all().values()
    jasonApi = {

        # 'nav_index': data_source.nav(request)['_index_'],
        # 'nav_nav': data_source.nav(request)['_nav_'],
        # 'nav_account': data_source.nav(request)['_account_'],

        'yes': data_source.DataForm.editListing(request, asin),
        # 'test': test,
        # 'user_account': userAccount(request),
    }

    return render(request, 'yes.html', jasonApi)



def upData(request):
    jasonApi = {
        'page_id': 'upData',

        'nav_index': data_source.nav(request)['_index_'],
        'nav_nav': data_source.nav(request)['_nav_'],
        'nav_account': data_source.nav(request)['_account_'],

        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': detailImg('B09YLLXKDT'),
        'user_account': userAccount(request),
    }

    return render(request, 'order.html', jasonApi)


'''
START---Moulde: Admin | Manager Product List | Edit Listing | Edit Index
'''
def _admin_(request):
    user_id = request.GET.get('user_id')
    # asin = asin_transfer
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],

        'listing': models.Listing.objects.all().values(),
        'manager': 'admin&=jessie&manager',
        'edit_index': 'admin&=jessie&editIndex',
    }

    return render(request, 'admin.html', jasonApi)


def managerProductList(request):
    user_id = request.GET.get('user_id')
    # asin = asin_transfer
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],

        'listing': models.Listing.objects.all().values(),
        'admin': 'adminjessie',

    }

    return render(request, 'manager-product-list.html', jasonApi)


def editListing(request, asin):
    user_id = request.GET.get('user_id')
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],

        # 'url': 'admin&edit=',
        'asin': asin,

        'listing': models.Listing.objects.filter(asin=asin).values()[0],
        'bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
        'len_bullet_point': len(eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point'])),
        'manager': 'admin&=jessie&manager',
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
        'status': data_source.DataForm.editListing(request, asin),
        'view': 'products&asin=' + asin,
        'again': 'admin&edit=' + asin,
        'manager': 'admin&=jessie&manager',
        'img': '/static/image/yeah/ok.jpg',
    }

    return render(request, 'yes.html', jasonApi)


def editIndex(request):
    user_id = request.GET.get('user_id')
    product_description = models.ProductDescription.objects.all().values()
    
    jasonApi = {

        'nav_index': data_source.nav(user_id)['_index_'],
        'nav_nav': data_source.nav(user_id)['_nav_'],
        'nav_account': data_source.nav(user_id)['_account_'],

        'admin': 'admin&=jessie',
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
            'manager': 'admin&=jessie&editIndex',
            'img': '/static/image/yeah/yeah.jpg'
        }

    return render(request, 'yes.html', jasonApi)
'''
END---Moulde: Admin | Manager Product List | Edit Listing | Edit Index
'''

'''
START---verify: signUp | login
'''
def userAccount(request):
    user_login = {
        'email' : request.POST.get('email'),
        'password' : request.POST.get('passWord'),
    }
    user_account_db = models.UserAccount.objects.all().values('email','password')
    print('user_login:',user_login)
    try:
        for user_account in user_account_db:
            print('user_account_db:',user_account)
            if user_login == user_account:
                print('>>>',user_account, user_account['email'])
                # user_account = list(user_account.values())[0]
                # return HttpResponse(user_account['email'])
                return user_account['email']
            else:
                pass
    except:
        return None
    jasonApi = {

        }
    return render(request, 'yes.html', jasonApi)
'''
END---verify: signUp | login
'''



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
CreateUserAccount addAccount addUserInfo addCart addOder
'''
class CreateUserAccount:
    pass




'''
check Asin between AsinInfo DB and CSV, if new, update table AsinInfo
'''
asin_csv_list = data_source.DataCSV.asinList()
asin_db_list = data_source.AsinDB.asinList()
if len(asin_csv_list) == len(asin_db_list):
    '''
    the same csv and mySql_db, return None
    '''
    print('>>>>>> no new asin', '\n')

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
    print('>>>>>> have new asin... ', asin, 'saving...', '\n')
    # return new_asin_list

elif len(asin_csv_list) < len(asin_db_list):
    '''
    more mySql_db, delete different asin, and return asin list from mySql DB
    '''
    print('>>>>>> asin_csv_list less than asin_db_list, Check it!')
else:
    print('>>>>>> error..., Check Please!')


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
    # if models.ProductDescription.objects.all():
    #     print('Table ProductDescription is',True)
    #     db_table_index = models.ProductDescription.objects.get(id=data_source.DataForm.getIndexData(request)['id'])
    #     db_table_index.asin = data_source.DataForm.getIndexData(request)['asin']
    #     db_table_index.bullet_point_01 = data_source.DataForm.getIndexData(request)['bullet_point_01']
    #     db_table_index.bullet_point_02 = data_source.DataForm.getIndexData(request)['bullet_point_02']
    #     db_table_index.bullet_point_03 = data_source.DataForm.getIndexData(request)['bullet_point_03']
    #     db_table_index.url = data_source.DataForm.getIndexData(request)['url']
    #     db_table_index.save()

    #     return 'Yeah, Save success!'
    # else:
    #     print('Table ProductDescription is',False)
    #     models.ProductDescription.objects.create(
    #         # id = models.ProductDescription.objects.get(id=data_source.DataForm.getIndexData(request)['id']),
    #         asin = data_source.DataForm.getIndexData(request)['asin'],
    #         bullet_point_01 = data_source.DataForm.getIndexData(request)['bullet_point_01'],
    #         bullet_point_02 = data_source.DataForm.getIndexData(request)['bullet_point_02'],
    #         bullet_point_03 = data_source.DataForm.getIndexData(request)['bullet_point_03'],
    #         url = data_source.DataForm.getIndexData(request)['url']
    #     )

    #     return 'Create it done!'





# print(images.urlAsinImg(asin_db_list))


# def setFirstImg(asin):
#     tag = images.urlAsinImg(data_source.AsinDB.asinList())[asin]['7']
#     for first_img_url in tag:
#         if '00-' in first_img_url:
#             return first_img_url
#         else:
#             pass

print('>>>>>> from DB, Total:', len(asin_db_list), '\n', asin_db_list, '\n')




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







