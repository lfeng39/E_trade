from django.db import models
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import datetime, time
import pandas as pd
import os
from JAL import images
from JAL import data_source

'''
Create MySQL DB Table
'''
class UserAccount(models.Model):
    user_id = models.CharField(max_length = 20, blank=True)
    user_name = models.CharField(max_length = 20, blank=True)
    email = models.EmailField(max_length = 30, blank=False) # false：必填
    password = models.CharField(max_length = 20, blank=False)
    first_name = models.CharField(max_length = 20, blank=True)
    last_name = models.CharField(max_length = 20, blank=True)
    address = models.CharField(max_length = 300, blank=True)
    street = models.CharField(max_length = 300, blank=True)
    ctiy = models.CharField(max_length = 20, blank=True)
    country = models.CharField(max_length = 20, blank=True)
    code = models.CharField(max_length = 5, blank=True)

class AsinInfo(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    sku = models.CharField(max_length=30, blank=True)
    sku_sn = models.CharField(max_length=50, blank=True)

class ProductInfo(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    sku = models.CharField(max_length=30, blank=True)
    sku_sn = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=300, blank=True)
    price = models.IntegerField()
    bullet_point = models.CharField(max_length=3000, blank=True)
    description = models.TextField(max_length=500, blank=True)
    first_img = models.CharField(max_length=300, blank=True)

class ProductDescription(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    bullet_point_00 = models.CharField(max_length=500, blank=True)
    bullet_point_01 = models.CharField(max_length=500, blank=True)
    bullet_point_02 = models.CharField(max_length=500, blank=True)
    bullet_point_03 = models.CharField(max_length=500, blank=True)
    bullet_point_04 = models.CharField(max_length=500, blank=True)
    bullet_point_05 = models.CharField(max_length=500, blank=True)
    bullet_point_06 = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=500, blank=True)

class Image(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    listing_7 = models.CharField(max_length=140, blank=True)
    A_970 = models.CharField(max_length=140, blank=True)
    A_300 = models.CharField(max_length=140, blank=True)

class SalesStatus(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    new = models.IntegerField()
    onSale = models.IntegerField()
    unavailabe = models.IntegerField()
    restock = models.IntegerField()

class Cart(models.Model):
    user_id = models.CharField(max_length = 20, blank=False)
    asin = models.CharField(max_length=10, blank=True)

class Order(models.Model):
    order_id = models.CharField(max_length = 20, blank=False)
    user_id = models.CharField(max_length = 20, blank=False)


'''
Check Asin
# '''
# class LatestAsin():
#     '''
#     get asin from MySql DB
#     '''
#     def asin_mySql_db():
#         asin_mySql = AsinInfo.objects.all()
#         asin_mySql_db = []
#         for i in asin_mySql:
#             asin_mySql_db.append(i.asin)

#         return asin_mySql_db

#     def saveAsin(new_asin):
#         AsinInfo.objects.create(
#             asin = new_asin,
#             sku = new_asin + '-tempName',
#             sku_sn = new_asin + '-tempName-',
#         )

#     '''
#     check new asin
#     '''
#     def checkNewAsin():
#         # initializa asin_csv
#         asin_csv = data_source.DataSource.getAsinCvs('asin')
#         if len(asin_csv) == len(LatestAsin.asin_mySql_db()):
#             '''
#             the same csv adn mySql, return None
#             '''
#             print('\n\n', '>>>>>> no new asin ===')

#             return 'None'

#         elif len(asin_csv) > len(LatestAsin.asin_mySql_db()):
#             '''
#             more csv, return new asin from csv
#             '''
#             new_asin_list = []
#             for asin in asin_csv:
#                 if asin in LatestAsin.asin_mySql_db():
#                     pass
#                 else:
#                     new_asin_list.append(asin)
#             print(' >>>>>> have new asin... saving... ===')

#             return new_asin_list

#         elif len(asin_csv) < len(LatestAsin.asin_mySql_db()):
#             '''
#             more mySql DB, delete different asin, and return asin list from mySql DB
#             '''
#             try:
#                 AsinInfo.objects.filter(id='392').delete()
#             except:
#                 print(' >>>>>> oh, somthing error... ===')
            
#             return LatestAsin.asin_mySql_db()


# '''
# Save Products Data From CSV to MySQL DB
# '''
# # initializa newAsin
# have_new_asin = LatestAsin.checkNewAsin()
# # have_new_asin = 'None'
# # def saveAsin():
# if have_new_asin == 'None':
#     pass
# else:
#     for new_asin in have_new_asin:
#         AsinInfo.objects.create(
#             asin = new_asin,
#             sku = new_asin + '-tempName',
#             sku_sn = new_asin + '-tempName-',
#         )
        
#         ProductDescription.objects.create(
#             asin = new_asin,
#             bullet_point_00 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][0],
#             bullet_point_01 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][1],
#             bullet_point_02 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][2],
#             bullet_point_03 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][3],
#             bullet_point_04 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][4],
#             bullet_point_05 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][5],
#             bullet_point_06 = data_source.parseCSV.bulletPoint(new_asin)['Bullet Point'][6],
#             description = data_source.parseCSV.__description__(new_asin)['Description'],
#         )

#         ProductInfo.objects.create(
#             asin = new_asin,
#             sku = new_asin + '-tempName',
#             sku_sn = new_asin + '-tempName-',
#             title = data_source.parseCSV.productTitle(new_asin)['Product Title'],
#             price = 39.99,
#             bullet_point = new_asin,
#             description = new_asin,
#             first_img = images.urlAsinImg(LatestAsin.asin_mySql_db())[new_asin]['7'][0],
#         )
#     print('\n', '>>>>>>', 'new asin add', '\n', have_new_asin)


# print('\n', '>>>>>>', 'from DB:', '\n', LatestAsin.asin_mySql_db(), '\n', images.urlAsinImg(LatestAsin.asin_mySql_db())['B0BM44ST75']['7'][0])

# print('user>>>>',UserAccount.objects.filter(email='lfeng').values())

# '''
# Global Variable
# '''
# _asin_ = LatestAsin.asin_mySql_db()
# product = _asin_
# page_id = ['index', 'about', 'products', 'myCart', 'login', 'signUp', 'order', 'account', 'myAccount', product]
# # print('look:>>>>>>',page_id[6])






# def detailImg(asin):

#     detail_img = {
#         'img_7_url': images.urlAsinImg(_asin_)[asin]['7'],
#         'img_970_url': images.urlAsinImg(_asin_)[asin]['970'],
#         'img_300_url': images.urlAsinImg(_asin_)[asin]['300'],
#     }

#     return detail_img



# '''
# index IMG
# '''
# img_show_dict = {}
# for i in range(len(_asin_)):
#     img_show_dict[_asin_[i]] = os.listdir('static/image/show/' + _asin_[i])

#     for k in range(len(img_show_dict[_asin_[i]])):
#         img_show_dict[_asin_[i]] = img_show_dict[_asin_[i]][k].replace('.jpg', '')



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
