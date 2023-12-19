print('\n>>> this is views.py <<< ')

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.utils import timezone
from urllib import request
import datetime, time, zoneinfo, pytz
import os
import re
from JAL import models, urls, spider, images, forms, verify, spider
import schedule

from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token


print('==============================================')
print('|  Part: user interface                      |')
print('|  index | brand | products                  |')
print('|                                            |')
print('|  Part: account module                      |')
print('|  login | signUp | verify                   |')
print('|                                            |')
print('|  Part: order cart module                   |')
print('|                                            |')
print('|  Part: manager module                      |')
print('|  edit index | edit listing | edit coupon   |')
print('|                                            |')
print('|  Part: check asin                          |')
print('|  csv & db                                  |')
print('|                                            |')
print('|  Part: save data                           |')
print('==============================================')



'''
=======================
|   Part: test url    |
=======================
'''
'''
local test url
'''
http = 'http://'
_ip_ = '127.0.0.1'
# csrftoken: Eoa1iSdBOEbaTTdopOt49k05uczyAPvv
# _ip_ = '0.0.0.0'
# csrftoken: T83BR0wnzOOGoGNuSw3mw9kOyQWif8Ns
_port_ = ':8000'
_app_ = '/JAL/'
base_url = http + _ip_ + _port_ + _app_
'''
server test url
'''
# huashengke
# _ip_ = '822u770q09.zicp.fun:44088'
# ngrok
_ip_ = '6c7d-103-84-219-16.ngrok-free.app'
# base_url = 'https://' + _ip_ + '/JAL/'
'''
Vultr server url
'''
# _ip_ = '140.82.22.68'
# _ip_ = '192.168.39.84'
_ip_ = ''
# base_url = 'https://' + _ip_ + '/JAL/'
print('oooooo Part: test url >>> url_now')
print('oooooo', base_url, '\n')
def nav():
    nav_dict = {
        '_index_' : 
        {
            'index': base_url + '',
            'includ_user_id_url': '',
        },

        '_nav_' : 
        {
            'Brand': base_url + 'brand',
            'Products': base_url + 'products',
            # 'admin': base_url + 'admin',
        },

        '_account_' : 
        {
            'cart': [base_url + 'cart', 'Cart'],
            'login': [base_url + 'login', 'Login'],
            'createAccount': [base_url + 'createAccount', 'Create Account'],
            'order': [base_url + 'order', 'Order'],
            'account': [base_url + 'account', 'Account'],
            'myAccount': [base_url + 'myAccount', 'MyAccount'],
        },
        '_admin_':
        {
            'Dashboard': base_url + 'admin' + 'jessie',
            'Listing': base_url + 'admin' + 'jessie' + '&listing',
            'Promote': base_url + 'admin' + 'jessie' + '&promote',
            'CouponRelease': base_url + 'admin' + 'jessie' + '&coupon',
        },
    }
    return nav_dict



'''
===============================
|   Part: user interface      |
|   index | brand | products  |
===============================
'''
def test(request):
    htmlApi = {
        'page_id': 'test',
        'nav_index': nav()['_index_'],
        'nav_nav': nav()['_nav_'],
        'nav_account': nav()['_account_'],

        'timezone': spider.time_zone,
    }
    return render(request, 'test.html', htmlApi)




'''
===========================================================================================================================
|   Object Product: _shelf_ _lisitng_ manageListing editListing addAsin addListing addFirstImg addSevenImg addAPlusImg    |
===========================================================================================================================
'''
class Product:
    '''
    veiws products
    '''
    def _shelf_ (request):
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
        get all products info, but status is '00'
        '''
        product_info = models.Listing.objects.filter(status='01')

        htmlApi = {
            'page_id': 'products',

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],
            # 'csrftoken': csrftoken,

            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            # '''
            # products module
            # '''
            'lenth': len(product_info),
            'product_info': product_info,

            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'products.html', htmlApi)
    '''
    veiws listing
    '''
    def _listing_(request, asin):
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
            'page_id': asin,

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],
            # 'csrftoken': csrftoken,

            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            'img_7': images.Img.imgUrl(asin, '7'),
            'product_img': detailImg(asin),
            'product_info': models.Listing.objects.filter(asin=asin).values()[0],
            ### the data tpye is 'str' that got from DB
            ### method eval() can changed 'str' to 'list' or 'dict'
            'product_bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
            'product_description': models.Listing.objects.filter(asin=asin).values()[0],
            'sales_status': '',
            'cupon': '',
            'amazon': 'https://www.amazon.com/dp/' + asin,

            # '''
            # footer-timezone
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'listing.html', htmlApi)
    '''
    manage listing
    '''
    def manageListing(request):
        '''
        get session
        '''
        user_status = request.session.get('user_status')
        user_email = request.session.get('user_email')
        # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)

        htmlApi = {
            'page_id': 'manager',

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],
            'nav_admin': nav()['_admin_'],

            # '''
            # account module
            # '''
            # 'user_status': user_status,
            'user_account': user_email,
            # 'user_name': user_name[0][0],

            'listing': models.Listing.objects.all().values(),
            
            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'manage-product.html', htmlApi)
    @csrf_protect
    @csrf_exempt
    @requires_csrf_token
    def editListing(request, asin):
        if request.method == 'GET':
            '''
            get session
            '''
            user_status = request.session.get('user_status')
            user_email = request.session.get('user_email')
            # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)
            
            htmlApi = {
                'page_id': 'editListing',

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],
                'nav_admin': nav()['_admin_'],

                # '''
                # account module
                # '''
                # 'user_status': user_status,
                'user_account': user_email,
                # 'user_name': user_name[0][0],

                'asin': asin,
                'listing': models.Listing.objects.filter(asin=asin).values()[0],
                'bullet_point': eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point']),
                'len_bullet_point': len(eval(models.Listing.objects.filter(asin=asin).values()[0]['bullet_point'])),
                'edit_listing': nav()['_admin_']['Listing'],
                
                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'edit-listing.html', htmlApi)
        if request.method == 'POST':
            # return HttpResponse('JAL')
            htmlApi = {
                'page_id': 'editListingDone',
                'listing_edit': True,

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],

                # '''
                # account module
                # '''
                # 'status': spider.DataForm.editListing(request, asin),
                'tip': Product.saveListing(request, asin),
                'view': 'products&asin=' + asin,
                'again': nav()['_admin_']['Listing'] + '=' + asin,
                'back': nav()['_admin_']['Listing'],
                'img': '/static/image/yeah/ok.jpg',
                
                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'done.html', htmlApi)
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
            title = spider.DataCSV.listingTitle(asin)['Product Title'],
            price = 39.99,
            bullet_point = spider.DataCSV.bulletPoint(asin)['Bullet Point'],
            description = spider.DataCSV.__description__(asin)['Description'],
            first_img = images.Img.firstImg(asin, '7'),
            status = '01',
        )
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
            return 'Listing Save done'
        except:
            error = asin + ' is not in productlist, please try again...'
            return error
    def addImgUrl(asin):
        pass



'''
===========================================================================================================
|   Object Promote: _index_ managePromote createPromote editPromote _counpon_ _calculate_ createCoupon    |
===========================================================================================================
'''
class Promote:
    '''
    index
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

        try:
            promote_info = models.Promote.objects.all().values()[0]
        except:
            promote_info = ''
        # print(promote_info)
        htmlApi = {
            'page_id': 'index',

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],

            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,
            # 'csrftoken': csrftoken,

            # '''
            # promote-banner
            # '''
            'promote_info': promote_info,

            # '''
            # promote-sku
            # '''
            'asin_code': asin_db_list,
            'includ_user_id_url': nav()['_index_']['includ_user_id_url'],
            # 6 is B0BRHWQ27R
            'product_info': models.Listing.objects.all().values(),
            'product_info_title': models.Listing.objects.all().values()[6]['title'].split('-'),

            'img_name': img_show_dict,
            'product_bullet_point': eval(models.Listing.objects.filter(asin='B0BRHWQ27R').values()[0]['bullet_point']),

            # '''
            # footer-timezone
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'index.html', htmlApi)

    def managePromote(request):
        '''
        get session
        '''
        user_status = request.session.get('user_status')
        user_email = request.session.get('user_email')
        # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)

        promote_info = models.Promote.objects.all().values()
        print(promote_info)
        htmlApi = {
            'page_id': 'editIndex',

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],
            'nav_admin': nav()['_admin_'],

            # '''
            # account module
            # '''
            'admin_account': user_email,

            'admin': 'adminjessie',
            'id': promote_info,
            'promote_info': promote_info,
            'bullet_point': promote_info,
            'tips': 'tips',

            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'manage-promote.html', htmlApi)
    # def savePromote(request):
    #     get_index_data = forms.getIndexData(request)
    #     try:
    #         '''
    #         save
    #         '''
    #         db_table_promote = models.Promote.objects.get(promote_code=get_index_data['promote_code'])
    #         # db_table_promote.promote_type = aaa
    #         db_table_promote.promote_img = get_index_data['promote_img']
    #         db_table_promote.bullet_point_01 = get_index_data['bullet_point_01']
    #         db_table_promote.bullet_point_02 = get_index_data['bullet_point_02']
    #         db_table_promote.bullet_point_03 = get_index_data['bullet_point_03']
    #         db_table_promote.promote_url = get_index_data['promote_url']
    #         db_table_promote.save()
    #         return 'Promote Save done'
    #     except:
    #         '''
    #         if False, create it
    #         '''
    #         models.Promote.objects.create(
    #             promote_type = get_index_data['promote_type'],
    #             promote_code = get_index_data['promote_code'],
    #             promote_img = get_index_data['promote_img'],
    #             bullet_point_01 = get_index_data['bullet_point_01'],
    #             bullet_point_02 = get_index_data['bullet_point_02'],
    #             bullet_point_03 = get_index_data['bullet_point_03'],
    #             promote_url = get_index_data['promote_url']
    #         )
    #         return 'Promote Create done'
    # def createPromote(request):
    #     get_index_data = forms.getIndexData(request)
    #     try:
    #         '''
    #         if False, create it
    #         '''
    #         models.Promote.objects.create(
    #             promote_type = get_index_data['promote_type'],
    #             promote_code = get_index_data['promote_code'],
    #             promote_img = get_index_data['promote_img'],
    #             bullet_point_01 = get_index_data['bullet_point_01'],
    #             bullet_point_02 = get_index_data['bullet_point_02'],
    #             bullet_point_03 = get_index_data['bullet_point_03'],
    #             promote_url = get_index_data['promote_url']
    #         )
    #         return 'Promote Create done'
    #     except:
    #         return 'create error'
    @csrf_protect
    @csrf_exempt
    @requires_csrf_token
    def createPromote(request):
        if request.method == 'GET':
            '''
            get session
            '''
            user_status = request.session.get('user_status')
            user_email = request.session.get('user_email')
            # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)

            # promote_info = models.Promote.objects.all().values()
            # promote_info = models.Promote.objects.filter(promote_code=code).values()
            htmlApi = {
                'page_id': 'editIndex',
                'protome_create': True,

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],
                'nav_admin': nav()['_admin_'],

                # '''
                # account module
                # '''
                'admin_account': True,


                'admin': 'adminjessie',
                # 'id': promote_info,
                # 'promote_info': promote_info,
                'manage_promote': nav()['_admin_']['Promote'],

                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'create-promote.html', htmlApi)
        if request.method == 'POST':
            get_index_data = forms.getIndexData(request)
            # try:
            '''
            if False, create it
            '''
            models.Promote.objects.create(
                type = get_index_data['promote_type'],
                code = get_index_data['promote_code'],
                img = get_index_data['promote_img'],
                url = get_index_data['promote_url'],
                channel = get_index_data['promote_channel'],
                bullet_point_01 = get_index_data['bullet_point_01'],
                bullet_point_02 = get_index_data['bullet_point_02'],
                bullet_point_03 = get_index_data['bullet_point_03'],
            )
            #     return 'Promote Create done'
            # except:
            #     return 'create error'
            
            htmlApi = {
                'page_id': 'editPromoteDone',
                'protome_create': True,

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],

                # 'tip': Promote.createPromote(request),
                'tip': 'Promote Create done',
                'back': nav()['_admin_']['Promote'],
                'img': '/static/image/yeah/yeah.jpg',

                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'done.html', htmlApi)
    @csrf_protect
    @csrf_exempt
    @requires_csrf_token
    def editPromote(request, code):
        if request.method == 'GET':
            '''
            get session
            '''
            user_status = request.session.get('user_status')
            user_email = request.session.get('user_email')
            # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)

            # promote_info = models.Promote.objects.all().values()
            promote_info = models.Promote.objects.filter(promote_code=code).values()

            htmlApi = {
                'page_id': 'editIndex',

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],
                'nav_admin': nav()['_admin_'],
                
                'admin_account': True,

                'admin': 'adminjessie',
                'id': promote_info,
                'promote_info': promote_info,
                'manage_promote': nav()['_admin_']['Promote'],
                
                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'edit-promote.html', htmlApi)
        if request.method == 'POST':
            get_index_data = forms.getIndexData(request)
            '''
            save
            '''
            db_table_promote = models.Promote.objects.get(promote_code=get_index_data['promote_code'])
            # db_table_promote.promote_type = aaa
            db_table_promote.promote_img = get_index_data['promote_img']
            db_table_promote.promote_url = get_index_data['promote_url']
            db_table_promote.promote_channel = get_index_data['promote_channel']
            db_table_promote.bullet_point_01 = get_index_data['bullet_point_01']
            db_table_promote.bullet_point_02 = get_index_data['bullet_point_02']
            db_table_promote.bullet_point_03 = get_index_data['bullet_point_03']
            db_table_promote.save()
            htmlApi = {
                'page_id': 'editPromoteDone',
                'protome_create': True,

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],

                'tip': 'Promote Save done',
                'back': nav()['_admin_']['Promote'],
                'img': '/static/image/yeah/yeah.jpg',
                
                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'done.html', htmlApi)
    def _coupon_(request):
        coupon_dataDB = models.Coupon.objects.all().values()
        htmlApi = {
            'page_id': 'coupon',
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_admin': nav()['_admin_'],

            'coupon_info': coupon_dataDB,
            
            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'manage-coupon.html', htmlApi)
    def _calculate_(amount, coupon):
        amount = float(amount)
        coupon = float(coupon)
        if coupon > 1:
            off_price = '{:.2f}'.format(amount - coupon )
            return off_price
        if coupon < 1:
            off_price = '{:.2f}'.format(amount * ( 1 - coupon ))
            return off_price
    # def createCoupon(request):
    #     get_coupon_info = forms.getCouponData(request)

    #     # if get_coupon_info['cash']:
    #     #     pass

    #     models.Coupon.objects.create(     
    #         asin = 'ALL',
    #         sku = 'ALL',
    #         title = get_coupon_info['title'],
    #         coupon_code = get_coupon_info['code'],
    #         type_cash = get_coupon_info['cash'],
    #         type_percentage = float(0),
    #         # type_percentage = float(get_coupon_info['percentage'])/100,
    #         start_at = spider.time_zone,
    #         end_at = spider.time_zone,
    #         type_status = '01',
    #     )
    #     return 'Coupon Create done'
    @csrf_protect
    @csrf_exempt
    @requires_csrf_token
    def createCoupon(request):
        if request.method == 'GET':
            htmlApi = {
                'page_id': 'coupon',
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_admin': nav()['_admin_'],

                'time_date': spider.cityTime('America/Los_Angeles').strftime('%Y-%m-%d'),
                
                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'create-coupon.html', htmlApi)
        if request.method == 'POST':
            get_coupon_info = forms.getCouponData(request)
            models.Coupon.objects.create(     
                asin = 'ALL',
                sku = 'ALL',
                title = get_coupon_info['title'],
                coupon_code = get_coupon_info['code'],
                type_cash = get_coupon_info['cash'],
                type_percentage = float(0),
                # type_percentage = float(get_coupon_info['percentage'])/100,
                start_at = spider.time_zone,
                end_at = spider.time_zone,
                status = '01',
            )
            htmlApi = {
                'page_id': 'editListingDone',
                'counpon_create': True,

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],

                'tip': 'Coupon Create done',
                'back': nav()['_admin_']['CouponRelease'],
                'img': '/static/image/yeah/ok.jpg',
                
                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'done.html', htmlApi)




'''
==================================================================
|   CreateUserAccount: addAccount addUserInfo addCart addOder    |
==================================================================
'''
class UserAccount:
    def addUserAccount(request):
        get_account_info = forms.getAccountInfo(request)
        models.UserAccount.objects.create(
            user_id = spider.generate_random_8_digit(),
            user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', get_account_info['email'])[0],
            email = get_account_info['email'],
            password = get_account_info['password'],
            email_platform = re.findall(r'@([a-zA-Z0-9_.+-]+)', get_account_info['email'])[0],
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
            # db_table_useraccount.user_name = get_account_info['user_name']
            # db_table_useraccount.password = get_account_info['password']
            # db_table_useraccount.first_name = get_account_info['first_name']
            # db_table_useraccount.last_name = get_account_info['last_name']
            db_table_useraccount.address = get_account_info['address']
            db_table_useraccount.street = get_account_info['street']
            db_table_useraccount.city = get_account_info['city']
            db_table_useraccount.country = get_account_info['country']
            db_table_useraccount.code = get_account_info['code']
            db_table_useraccount.save()
            return 'Account Save done'
        except:
            error = str(user_email) + ' please try again...'
            return error
    '''
    save data after edit account
    '''
    def saveAccount(request, user_email, module):
        get_account_info = forms.getAccountInfo(request)
        try:
            if module == 'shipping':
                '''
                save the data that has been changed from edit.html to DB
                '''
                db_table_useraccount = models.UserAccount.objects.get(email=user_email)
                db_table_useraccount.first_name = get_account_info['first_name']
                db_table_useraccount.last_name = get_account_info['last_name']
                db_table_useraccount.address = get_account_info['address']
                db_table_useraccount.street = get_account_info['street']
                db_table_useraccount.city = get_account_info['city']
                db_table_useraccount.country = get_account_info['country']
                db_table_useraccount.code = get_account_info['code']
                db_table_useraccount.save()
                return 'Shipping info save done'
            if module == 'id':
                '''
                save the data that has been changed from edit.html to DB
                '''
                db_table_useraccount = models.UserAccount.objects.get(email=user_email)
                db_table_useraccount.user_name = get_account_info['user_name']
                db_table_useraccount.password = get_account_info['password']

                db_table_useraccount.save()
                return 'Account ID Save done'
        except:
            error = str(user_email) + ' please try again...'
            return error



class Brand:
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
            
            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],
            # 'csrftoken': csrftoken,

            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'about.html', htmlApi)



'''
===============================
|   Part: account module      |
|   Login | SignUp | Verify   |
===============================
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

        # '''
        # nav module
        # '''
        'nav_index': nav()['_index_'],
        'nav_nav': nav()['_nav_'],
        'nav_account': nav()['_account_'],
        # 'csrftoken': csrftoken,

        # '''
        # account module
        # '''
        'user_status': user_status,
        'user_account': user_email,
        'user_name': user_name,

        'account_email': {'email':'Email'},

        # '''
        # footer-timezone
        # '''
        'timezone': spider.time_zone,
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



@csrf_protect
@csrf_exempt
@requires_csrf_token
def verifyAccountDone(request):
    '''
    verify account valid
    '''
    account_form = forms.AccountDataForm(request.POST)
    '''
    account is not valid
    '''
    if not account_form.is_valid():
        htmlApi = {
            'page_id': 'login',

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],
            # 'csrftoken': csrftoken,

            # 'user_status': user_status,
            # 'user_account': user_email,
            # 'user_name': user_name,
            # 'account_email': {'email':'Email'},

            'msg': account_form.errors,
            'products': 'products',

            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'login.html', htmlApi)
    else:
        '''
        account is valid, verify exist
        '''
        verify_user_account = verify.VerifyAccount.verifyEmail(request)
        verify_user_password = verify.VerifyAccount.verifyPassWord(request)

        '''
        login success, set session, and redirect to index or other page
        '''
        if verify_user_password == True:
            # '''
            # # set_cookie
            #     # key : cookie的名称
            #     # value : 保存的cookie的值
            #     # max_age: 保存的时间，以秒为单位
            #     # expires: 过期时间，为datetime对象或时间字符串
            # '''
            # _urls_ = nav(verify_user_account[1])['_account_']['myAccount'][0]
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
            request.session.set_expiry(10800)
            _urls_ = nav()['_account_']['account'][0]
            return redirect(_urls_)
        '''
        login error, account is not exist
        '''
        if verify_user_account[0] == False:
            # CreateUserAccount.addUserAccount(request)
            htmlApi = {
                'page_id': 'login',
                
                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],
                # 'user_status': user_status,
                # 'user_account': user_email,
                # 'user_name': user_name,

                'email_tip': verify_user_account[1] + ' is not exist',
                # 'account_email': account_form.cleaned_data,

                'products': 'products',

                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'login.html', htmlApi)
        '''
        password error, again
        '''
        if verify_user_password == False:
            # CreateUserAccount.addUserAccount(request)
            htmlApi = {
                'page_id': 'login',

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],
                # 'user_status': user_status,
                # 'user_account': user_email,
                # 'user_name': user_name,

                'password_tip': 'Password error',
                'account_email': account_form.cleaned_data,

                'products': 'products',

                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
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

    '''
    user not online, redirect 'Login'
    '''
    if not user_status:
        user_name = 'Login'
        urls_index = nav()['_account_']['login'][0]
        rep = redirect(urls_index)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        user_account = models.UserAccount.objects.filter(email=user_email).values()[0]
        htmlApi = {
            'page_id': 'account',

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],

            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_account['user_name'],

            'user_account': user_account,
            'bag': False,
            'user_coupon': models.Coupon.objects.filter(status='01').values(),

            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'account.html', htmlApi)


@csrf_protect
@csrf_exempt
@requires_csrf_token
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

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],
            # 'csrftoken': csrftoken,

            'account_email': {'email':'Email'},

            # '''
            # footer-timezone
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'create-account.html', htmlApi)
    if request.method == 'POST':
        '''
        verify account valid
        '''
        # is_valid = forms.AccountDataForm(request.POST)
        account_form = forms.AccountDataForm(request.POST)
        if account_form.is_valid():
            '''
            account is valid, verify exist
            '''
            verify_user_account = verify.VerifyAccount.verifyEmail(request)
            verify_user_password = verify.VerifyAccount.verifyPassWord(request)

            '''
            account is exist, retry
            '''
            if verify_user_account[0] == True:
                # CreateUserAccount.addUserAccount(request)
                htmlApi = {
                    'page_id': 'createAccount',

                    # '''
                    # nav module
                    # '''
                    'nav_index': nav()['_index_'],
                    'nav_nav': nav()['_nav_'],
                    'nav_account': nav()['_account_'],
                    # 'csrftoken': csrftoken,

                    # 'user_status': user_status,
                    # 'user_account': user_email,
                    # 'user_name': user_name,

                    'tip': verify_user_account[1] + ' is exist',
                    'products': 'products',

                    # '''
                    # footer-timezone
                    # '''
                    'timezone': spider.time_zone,
                }
                return render(request, 'create-account.html', htmlApi)
            '''
            account is not exist, create it
            '''
            if verify_user_account[0] == False:
                UserAccount.addUserAccount(request)
                '''
                set_session, after created account
                '''
                request.session['user_status'] = True
                request.session['user_email'] = verify_user_account[1]

                htmlApi = {
                    # '''
                    # nav module
                    # '''
                    'nav_index': nav()['_index_'],
                    'nav_nav': nav()['_nav_'],
                    'nav_account': nav()['_account_'],
                    # 'csrftoken': csrftoken,

                    'account_create': True,
                    'user_status': True,
                    'user_account': verify_user_account[1],
                    # 'user_name': verify_user_account[1],
                    'user_name': re.findall(r'([a-zA-Z0-9_.+-]+)@', verify_user_account[1])[0],
                    
                    'tip': verify_user_account[1] + ' is created',
                    # 'account_email': account_form.cleaned_data,
                    'products': 'products',
                    'img': '/static/image/yeah/yeah.jpg',

                    # '''
                    # footer-timezone
                    # '''
                    'timezone': spider.time_zone,
                }
                return render(request, 'done.html', htmlApi)
        else:
            htmlApi = {
                'page_id': 'createAccount',

                # '''
                # nav module
                # '''
                'nav_index': nav()['_index_'],
                'nav_nav': nav()['_nav_'],
                'nav_account': nav()['_account_'],
                # 'csrftoken': csrftoken,
                # 'user_status': user_status,
                # 'user_account': user_email,
                # 'user_name': user_name,
                # 'account_emial': {'email':'Email'},

                'msg': account_form.errors,

                # '''
                # footer
                # '''
                'timezone': spider.time_zone,
            }
            return render(request, 'create-account.html', htmlApi)
@csrf_protect
@csrf_exempt
@requires_csrf_token
def editAccount(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    
    '''
    user not online, redirect 'Login'
    '''
    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    if request.method == 'GET':
        htmlApi = {
            'page_id': 'editAccount',
            'asin_code': asin_db_list,

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],

            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            'user_account': models.UserAccount.objects.filter(email=user_email).values()[0],
            
            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'edit-account.html', htmlApi)
    if request.method == 'POST':
        htmlApi = {
            'page_id': 'createAccountDone',
            'account_edit': True,

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],
            
            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            # 'tag': 'Your acount update  ',
            # 'status': DataForm.getIndexData(request),
            'tip': UserAccount.saveUserAccount(request, user_email),
            'back': nav()['_account_']['account'][0],
            # 'again': nav()['_admin_']['EditPromote'],
            'img': '/static/image/yeah/yeah.jpg',

            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'done.html', htmlApi)
@csrf_protect
@csrf_exempt
@requires_csrf_token
def editMyAccount(request, module):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    
    '''
    user not online, redirect 'Login'
    '''
    if not user_status:
        user_name = 'Login'
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']

    htmlApi = {
        'page_id': 'createAccountDone',
        'account_edit': True,

        # '''
        # nav module
        # '''
        'nav_index': nav()['_index_'],
        'nav_nav': nav()['_nav_'],
        'nav_account': nav()['_account_'],
        
        # '''
        # account module
        # '''
        'user_status': user_status,
        'user_account': user_email,
        'user_name': user_name,

        # 'tag': 'Your acount update  ',
        # 'status': DataForm.getIndexData(request),
        'tip': UserAccount.saveAccount(request, user_email, module),
        'back': nav()['_account_']['account'][0],
        # 'again': nav()['_admin_']['EditPromote'],
        'img': '/static/image/yeah/yeah.jpg',

        # '''
        # footer
        # '''
        'timezone': spider.time_zone,
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
        _url_ = nav()['_account_']['login'][0]
        rep = redirect(_url_)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        user_name = models.UserAccount.objects.filter(email=user_email).values()[0]['user_name']
        htmlApi = {
            'page_id': 'myCart',
            'asin_code': asin_db_list,

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],

            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            'product_info': models.Listing.objects.filter(asin='B0BTXB89PG').values()[0],
            'asin': detailImg('B0BTXB89PG'),
            'url_page_id_order': page_id[6],

            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }
        return render(request, 'my-cart.html', htmlApi)





'''
===============================
|   Part: order cart module   |
|   order | cart              |
===============================
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
        urls_index = nav()['_account_']['login'][0]
        rep = redirect(urls_index)
        # rep.set_cookie("is_login", True)
        return rep
    else:
        htmlApi = {
            'page_id': 'order',
            'asin_code': asin_db_list,

            # '''
            # nav module
            # '''
            'nav_index': nav()['_index_'],
            'nav_nav': nav()['_nav_'],
            'nav_account': nav()['_account_'],

            # '''
            # account module
            # '''
            'user_status': user_status,
            'user_account': user_email,
            'user_name': user_name,

            'product_info': models.Listing.objects.filter(asin='B0BTXB89PG').values()[0],
            'asin': detailImg('B0BTXB89PG'),

            # '''
            # footer
            # '''
            'timezone': spider.time_zone,
        }

        return render(request, 'order.html', htmlApi)






'''
===============================================
|   Part: manager module                      |
|   edit index | edit listing | edit coupon   |
===============================================
'''
def _admin_(request):
    '''
    get session
    '''
    user_status = request.session.get('user_status')
    user_email = request.session.get('user_email')
    # user_name = re.findall(r'([a-zA-Z0-9_.+-]+)@', user_email)
    
    htmlApi = {
        'page_id': 'adminjessie',

        # '''
        # nav module
        # '''
        'nav_index': nav()['_index_'],
        'nav_nav': nav()['_nav_'],
        'nav_account': nav()['_account_'],
        'nav_admin': nav()['_admin_'],

        # '''
        # account module
        # '''
        'admin_account': True,

        'listing': models.Listing.objects.all().values(),
        'edit_promote': 'adminjessie&editPromote',
        'edit_listing': 'adminjessie&edit-listing',

        # '''
        # footer
        # '''
        'timezone': spider.time_zone,
    }
    return render(request, 'admin.html', htmlApi)













'''
==============================================================================
|   Part: save data                                                          |
|   check Asin between AsinInfo DB and CSV, if new, update table AsinInfo    |
==============================================================================
'''
asin_csv_list = spider.DataCSV.asinList()
asin_db_list = spider.AsinDB.asinList()
print('oooooo Part: save data >>> from DB, length:', len(asin_db_list), '\n', asin_db_list, '\n')
if len(asin_csv_list) == len(asin_db_list):
    '''
    the same csv and mySql_db, return None
    '''
    print('oooooo Part: save data >>> no new asin', '\n')

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
            Product.addAsin(asin)
            Product.addListing(asin)
    print('oooooo Part: save data >>> have new asin... ', asin, 'saving...', '\n')
    # return new_asin_list

elif len(asin_csv_list) < len(asin_db_list):
    '''
    more mySql_db, delete different asin, and return asin list from mySql DB
    '''
    print('oooooo Part: save data >>> asin_csv_list less than asin_db_list, Check it!')
else:
    print('oooooo Part: save data >>> error..., Check Please!')



'''
check Listing from DB, if False, create it
'''
if models.Listing.objects.all():
    print('Table Listing is',True)
else:
    print('Table Listing is',False)
    for asin in asin_db_list:
        Product.addListing(asin)



# '''
# save data after edit index
# check ProductDescription from DB, if False, create it
# '''
# def saveIndexData(request):
#     get_index_data = forms.getIndexData(request)
#     try:
#         '''
#         save
#         '''
#         db_table_index = models.Promote.objects.get(id=get_index_data['id'])
#         db_table_index.asin = get_index_data['asin']
#         db_table_index.bullet_point_01 = get_index_data['bullet_point_01']
#         db_table_index.bullet_point_02 = get_index_data['bullet_point_02']
#         db_table_index.bullet_point_03 = get_index_data['bullet_point_03']
#         db_table_index.url = get_index_data['url']
#         db_table_index.save()
#         # print('00000000',db_table_index)
#         return 'Yeah, Save success!'
#     except:
#         '''
#         if False, create it
#         '''
#         models.Promote.objects.create(
#             id = get_index_data['id'],
#             promote_code = get_index_data['promote_code'],
#             bullet_point_01 = get_index_data['bullet_point_01'],
#             bullet_point_02 = get_index_data['bullet_point_02'],
#             bullet_point_03 = get_index_data['bullet_point_03'],
#             promote_url = get_index_data['promote_url']
#         )
#         return 'Create it done!'




'''
Global Variable
'''
page_id = ['index', 'about', 'products', 'myCart', 'login', 'signUp', 'order', 'account', 'myAccount', asin_db_list]
# print('look:>>>>>>',page_id[6])



def detailImg(asin):

    detail_img = {
        'img_7_url': images.urlAsinImg()[asin]['7'], 
        'img_970_url': images.urlAsinImg()[asin]['970'],
        'img_300_url': images.urlAsinImg()[asin]['300'],
    }

    return detail_img



from django.template.loader import render_to_string
def htmlMsg():
    SHA = spider.cityWeather('Shanghai')
    LON = spider.cityWeather('London')
    NYC = spider.cityWeather('New York')
    LAX = spider.cityWeather('Los Angeles')
    city_info = {
        # 'Shanghai': {'city':'SHA', 'time': spider.shanghai_time, 'temp': SHA['temp'], 'description': SHA['description']},
        # 'London': {'city':'LON', 'time': spider.lon_time, 'temp': LON['temp'], 'description': LON['description']},
        # 'NewYork': {'city':'NYC', 'time': spider.nyc_time, 'temp': NYC['temp'], 'description': NYC['description']},
        # 'LosAngeles': {'city':'LAX', 'time': spider.lax_time, 'temp': LAX['temp'], 'description': LAX['description']},
        'Shanghai': {'city':'SHA', 'time': datetime.datetime.now(tz=spider._shanghai_).strftime(spider._format_), 'temp': SHA['temp'], 'description': SHA['description']},
        'London': {'city':'LON', 'time': datetime.datetime.now(tz=spider._lon_).strftime('%Y-%m-%d %H:%M:%S %Z %z'), 'temp': LON['temp'], 'description': LON['description']},
        'NewYork': {'city':'NYC', 'time': datetime.datetime.now(tz=spider._nyc_).strftime('%Y-%m-%d %H:%M:%S %Z %z'), 'temp': NYC['temp'], 'description': NYC['description']},
        'LosAngeles': {'city':'LAX', 'time': datetime.datetime.now(tz=spider._lax_).strftime(spider._format_), 'temp': LAX['temp'], 'description': LAX['description']},
    }

    htmlApi = {
        'page_id': 'htmlMsg',
        'nav_index': nav()['_index_'],
        'nav_nav': nav()['_nav_'],
        'city': ['Los Angeles', 'New York', 'London', 'Shanghai'],
        'city_info': city_info,
    }
    return render_to_string('html-msg.html', htmlApi)

