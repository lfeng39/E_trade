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

print('\n>>> this is views.py <<< ')

def _index_(request):
    data_source.test(request)
    user = request.GET.get('user_id')
    jasonApi = {
        'asin_code': _asin_,

        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav(user)['_account_'],

        'includ_user_id_url': urls.nav(user)['_index_']['includ_user_id_url'],
        'product_info': models.ProductInfo.objects.all().values(),
        'product_asin': _asin_,
        'img_name': img_show_dict,
        'page_id': 'index',
        'user_account': user,
        # 'user_account': '',
    }
    print('index>>>',type(user),user)

    return render(request, 'index.html', jasonApi)

    

def _about_(request):
    user = request.GET.get('user_id')
    jasonApi = {

        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav('')['_account_'],

        'page_id': 'about',
        'user_account': user,
    }

    return render(request, 'about.html', jasonApi)
    


def _products_(request):
    user = request.GET.get('user_id')
    jasonApi = {

        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav('')['_account_'],

        'includ_user_id_url': urls.nav(user)['_index_']['includ_user_id_url'],
        # 'includ_user_id_url': '',
        # 'product_info': models.Listing.objects.all().values(),
        ### get all products info, but status is '00'
        'product_info': models.ProductInfo.objects.filter(status='01'),
        'page_id': 'products',
        'product_image': '',
        'product_title': '',
        'user_account': user,
        'abc': '%',
    }

    return render(request, 'products.html', jasonApi)



def _detail_(request, asin_transfer):
    user = request.GET.get('user_id')
    asin = asin_transfer
    jasonApi = {
        'page_id': asin,
        'product_img': detailImg(asin),

        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav('')['_account_'],

        'product_info': models.ProductInfo.objects.filter(asin=asin_transfer).values()[0],
        ### the data tpye is 'str' that got from DB
        ### method eval() can changed 'str' to 'list' or 'dict'
        'product_bullet_point': eval(models.Listing.objects.filter(asin=asin_transfer).values()[0]['bullet_point']),
        'product_description': models.ProductDescription.objects.filter(asin=asin_transfer).values()[0],
        'sales_status': '',
        'cupon': '',
        'user_account': userAccount(request),
        'amazon': 'https://www.amazon.com/dp/' + asin,
    }

    return render(request, 'detail.html', jasonApi)



def _login_(request):
    
    jasonApi = {

        'nav_index': urls.nav('')['_index_'],
        'nav_nav': urls.nav('')['_nav_'],
        'nav_account': urls.nav('')['_account_'],

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

        'nav_index': urls.nav('')['_index_'],
        'nav_nav': urls.nav('')['_nav_'],
        'nav_account': urls.nav('')['_account_'],

        'page_id': 'signUp',
        'user_account': userAccount(request),
    }

    return render(request, 'sign-up.html', jasonApi)



def _account_(request):
    
    jasonApi = {
        'page_id': 'account',
        'asin_code': _asin_,

        'nav_index': urls.nav('')['_index_'],
        'nav_nav': urls.nav('')['_nav_'],
        'nav_account': urls.nav('')['_account_'],

        'asin': models.detailImg('B09YLLXKDT'),
        'user_account': userAccount(request),
    }

    return render(request, 'account.html', jasonApi)



def myAccount(request):

    user = request.GET.get('user_id')
    my_account = models.UserAccount.objects.filter(email=user).values()[0]

    jasonApi = {
        'page_id': 'myAccount',

        'nav_index': urls.nav(user)['_index_'],
        'nav_nav': urls.nav(user)['_nav_'],
        'nav_account': urls.nav('')['_account_'],

        'user_account': user,
        'my_account': my_account,
    }

    return render(request, 'my-account.html', jasonApi)



def myCart(request):
    
    jasonApi = {
        'page_id': 'myCart',
        'asin_code': _asin_,

        'nav_index': urls.nav('')['_index_'],
        'nav_nav': urls.nav('')['_nav_'],
        'nav_account': urls.nav('')['_account_'],

        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': models.detailImg('B09YLLXKDT'),
        'url_page_id_order': models.page_id[6],
        'user_account': userAccount(request),
    }

    return render(request, 'my-cart.html', jasonApi)



def _order_(request):

    jasonApi = {
        'page_id': 'order',
        'asin_code': _asin_,

        'nav_index': urls.nav(request)['_index_'],
        'nav_nav': urls.nav(request)['_nav_'],
        'nav_account': urls.nav(request)['_account_'],

        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': detailImg('B09YLLXKDT'),
        'user_account': userAccount(request),
    }

    return render(request, 'order.html', jasonApi)



def postData(request):

    data_source.DataForm.postAccountInfoSignUp(request)
    # data_source.verifyAccount(request)
    test = models.UserAccount.objects.all().values()

    jasonApi = {

        'nav_index': urls.nav(request)['_index_'],
        'nav_nav': urls.nav(request)['_nav_'],
        'nav_account': urls.nav(request)['_account_'],

        'yes': 'yes',
        'test': test,
        'user_account': userAccount(request),
    }

    return render(request, 'yes.html', jasonApi)



def upData(request):

    jasonApi = {
        'page_id': 'upData',

        'nav_index': urls.nav(request)['_index_'],
        'nav_nav': urls.nav(request)['_nav_'],
        'nav_account': urls.nav(request)['_account_'],

        'product_info': models.ProductInfo.objects.filter(asin='B09YLKWBMV').values()[0],
        'asin': detailImg('B09YLLXKDT'),
        'user_account': userAccount(request),
    }

    return render(request, 'order.html', jasonApi)


'''
Check Asin
'''
class LatestAsin():
    '''
    get asin from MySql DB
    '''
    def asin_mySql_db():
        asin_mySql = models.AsinInfo.objects.all()
        asin_mySql_db = []
        for i in asin_mySql:
            # print('aaaaaaa',i)
            asin_mySql_db.append(i.asin)

        return asin_mySql_db

    def saveAsin(new_asin):
        models.AsinInfo.objects.create(
            asin = new_asin,
            sku = new_asin + '-tempName',
            sku_sn = new_asin + '-tempName-',
        )

    '''
    check new asin
    '''
    def checkNewAsin():
        # initializa asin_csv
        asin_csv = data_source.DataSource.getAsinCvs('asin')
        if len(asin_csv) == len(LatestAsin.asin_mySql_db()):
            '''
            the same csv adn mySql, return None
            '''
            print('>>>>>> no new asin', '\n')

            return 'None'

        elif len(asin_csv) > len(LatestAsin.asin_mySql_db()):
            '''
            more csv, return new asin from csv
            '''
            new_asin_list = []
            for asin in asin_csv:
                if asin in LatestAsin.asin_mySql_db():
                    pass
                else:
                    new_asin_list.append(asin)
            print('>>>>>> have new asin... saving...', '\n')

            return new_asin_list

        elif len(asin_csv) < len(LatestAsin.asin_mySql_db()):
            '''
            more mySql DB, delete different asin, and return asin list from mySql DB
            '''
            try:
                # models.AsinInfo.objects.filter(id='392').delete()
                pass
            except:
                print('>>>>>> oh, somthing error...', '\n')
            
            return LatestAsin.asin_mySql_db()


'''
Save Products Data From CSV to MySQL DB
'''
# initializa newAsin
have_new_asin = LatestAsin.checkNewAsin()
# have_new_asin = 'None'
# def saveAsin():
def setFirstImg(asin):
    tag = images.urlAsinImg(LatestAsin.asin_mySql_db())[asin]['7']
    for first_img_url in tag:
        if '00-' in first_img_url:
            return first_img_url
        else:
            pass

if have_new_asin == 'None':
    pass
else:
    for new_asin in have_new_asin:
        models.AsinInfo.objects.create(
            asin = new_asin,
            sku = new_asin + '-tempName',
            sku_sn = new_asin + '-tempName-',
        )
        
        models.ProductDescription.objects.create(
            asin = new_asin,
            bullet_point_00 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][0],
            bullet_point_01 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][1],
            bullet_point_02 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][2],
            bullet_point_03 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][3],
            bullet_point_04 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][4],
            bullet_point_05 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][5],
            bullet_point_06 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][6],
            description = data_source.parseCSV.__description__(new_asin)['Description'],
        )

        models.ProductInfo.objects.create(
            asin = new_asin,
            sku = new_asin + '-tempName',
            sku_sn = new_asin + '-tempName-',
            title = data_source.parseCSV.productTitle(new_asin)['Product Title'],
            price = 39.99,
            bullet_point = new_asin,
            description = new_asin,
            first_img = setFirstImg(new_asin),
        )

        models.Listing.objects.create(
            asin = new_asin,
            sku = new_asin,
            sku_sn = new_asin,
            title = data_source.parseCSV.productTitle(new_asin)['Product Title'],
            price = 39.99,
            bullet_point = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'],
            description = data_source.parseCSV.__description__(new_asin)['Description'],
            status = '1',
        )

    print('>>>>>> new asin add', '\n', have_new_asin)


print('>>>>>> from DB, Total:', len(LatestAsin.asin_mySql_db()), '\n', LatestAsin.asin_mySql_db(), '\n')



'''
Global Variable
'''
_asin_ = LatestAsin.asin_mySql_db()
product = _asin_
page_id = ['index', 'about', 'products', 'myCart', 'login', 'signUp', 'order', 'account', 'myAccount', product]
# print('look:>>>>>>',page_id[6])






def detailImg(asin):

    detail_img = {
        'img_7_url': images.urlAsinImg(_asin_)[asin]['7'],
        'img_970_url': images.urlAsinImg(_asin_)[asin]['970'],
        'img_300_url': images.urlAsinImg(_asin_)[asin]['300'],
    }

    return detail_img



'''
index IMG
'''
img_show_dict = {}
for i in range(len(_asin_)):
    img_show_dict[_asin_[i]] = os.listdir('static/image/show/' + _asin_[i])

    for k in range(len(img_show_dict[_asin_[i]])):
        img_show_dict[_asin_[i]] = img_show_dict[_asin_[i]][k].replace('.jpg', '')



'''
VERIFY DATA
'''
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





