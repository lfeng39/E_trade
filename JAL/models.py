from django.db import models
import pandas as pd
import os
from JAL import forms

class UserAccount(models.Model):
    email = models.CharField(max_length = 20, blank = False)
    password = models.CharField(max_length = 20, blank = False)
    country = models.CharField(max_length = 20, blank = True)
    ctiy = models.CharField(max_length = 20, blank = True)
    address = models.CharField(max_length = 300, blank = True)
    code = models.CharField(max_length = 5, blank = True)
    first_name = models.CharField(max_length = 20, blank = True)
    last_name = models.CharField(max_length = 20, blank = True)

class Product(models.Model):
    asin = models.CharField(max_length=10)
    title = models.CharField(max_length=140)
    price = models.IntegerField()
    descri = models.TextField()


# Create your models here.
def nav(type):

    app_title = ['ME AND MR. LEO', 'About', 'Product', 'ZMH', 'YDJ', 'DDL', 'Login', 'Sign Up']
    url = ['index', 'about', 'product', 'B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR', 'login', 'signUp']

    nav = {
        'ME AND MR. LEO': 'index',
        'About': 'about',
        'Product': 'product',
        'ZMH': 'B09YLLXKDT',
        'YDJ': 'B09YLKWBMV',
        'DDL': 'B09KG4R3YR',
        'Login': 'login',
        'Sign Up': 'signUp',
    }

    if type == 'url':
        return url
    elif type == 'app_title':
        return app_title
    elif type == 'nav':
        return nav
    else:
        pass

'''
全局变量
'''
asin = ['B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR']
version = ['/v1.00', '/v1.01', '/v1.02']

data_file_01 = 'static/csv/' +  asin[0] + '.csv'
data_file_02 = 'static/csv/' +  asin[1] + '.csv'
data_file_03 = 'static/csv/' +  asin[2] + '.csv'

# listing图片名称数据字典
img_name_listing = {
        asin[0]: os.listdir('static/image/' + asin[0] + version[0] + '/7'),
        asin[1]: os.listdir('static/image/' + asin[1] + version[0] + '/7'),
        asin[2]: os.listdir('static/image/' + asin[2] + version[0] + '/7'),
    }
# A_plus图片名称数据字典
img_name_a_plus = {
        asin[0]: os.listdir('static/image/' + asin[0] + version[0] + '/a_plus'),
        asin[1]: os.listdir('static/image/' + asin[1] + version[0] + '/a_plus'),
        asin[2]: os.listdir('static/image/' + asin[2] + version[0] + '/a_plus'),
    }
# print(imgName_Listing['B09YLLXKDT'])
# show图片名称数据字典
img_show = os.listdir('static/image/show')
img_shower = []
for i in range(len(img_show)):
    img_shower.append('/static/image/show/' + img_show[i])
# print(imgShower)

'''
链接数据库-
'''
def conData(asin):

    if asin == 'B09YLLXKDT':
        data_listing = pd.read_csv(data_file_01, encoding = 'GBK', engine='python')
    elif asin == 'B09YLKWBMV':
        data_listing = pd.read_csv(data_file_02, encoding = 'GBK', engine='python')
    elif asin == 'B09KG4R3YR':
        data_listing = pd.read_csv(data_file_03, encoding = 'GBK', engine='python')
    # print(dataFile)
    
    return data_listing

def listingData(asin):

    '''
    通过asin获取产品listing数据，并以Dict类型返回
    {{ asin.listingImg }}
    {{ asin.ProductTitle }}
    '''

    listing_data = conData(asin)

    temp = []
    for i in range(1,9):
        temp.append(listing_data.iloc[i,1])
    # print(temp)
    listing_data = {
        'listingImg': '/static/image/' + asin + version[0] + '/7/' + img_name_listing[asin][0],
        'ProductTitle': temp[0],
        'BulletPoint': [temp[1],temp[2],temp[3],temp[4],temp[5]],
        'Description': temp[6],
        'a_plus_img': [1,2,3]
    }

    return listing_data, temp[0]
# print(listingData('B09YLLXKDT')[0])

def productInfo():

    '''
    获取各文件夹下的图片，将图片分类
    '''
    
    img_url = [
        '/static/image/' + asin[0] + version[0] + '/7/' + img_name_listing[asin[0]][0],
        '/static/image/' + asin[1] + version[0] + '/7/' + img_name_listing[asin[1]][0],
        '/static/image/' + asin[2] + version[0] + '/7/' + img_name_listing[asin[2]][0],
    ]

    a_plus_img_url = [
        '/static/image/' + asin[0] + version[0] + '/a_plus/' + os.listdir('static/image/' + asin[0] + version[0] + '/a_plus')[0],
        '/static/image/' + asin[1] + version[0] + '/a_plus/' + os.listdir('static/image/' + asin[1] + version[0] + '/a_plus')[0],
        '/static/image/' + asin[2] + version[0] + '/a_plus/' + os.listdir('static/image/' + asin[2] + version[0] + '/a_plus')[0],
    ]

    productInfo = {
        0: {'img': img_url[0], 'ProductTitle': listingData(asin[0])[1]},
        1: {'img': img_url[1], 'ProductTitle': listingData(asin[1])[1]},
        2: {'img': img_url[2], 'ProductTitle': listingData(asin[2])[1]},
        'url': [asin[0], asin[1], asin[2]]
    }

    return productInfo
# print(productInfo())

'''
SAVE DATA
'''
def saveData(request):
    
    getAccountInfo = forms.DataForm.getAccountInfo(request)

    receive = [getAccountInfo[0], getAccountInfo[1]]

    new_df = []
    new_df.append(receive)

    postData = pd.DataFrame(new_df)
    postData.to_csv('static/csv/account.csv')

    

    # print(len(new_df))
    print(postData)

'''
VERIFY DATA
'''
def verifyData():

    accountData = pd.read_csv('static/csv/account.csv')