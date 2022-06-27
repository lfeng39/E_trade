from ensurepip import version
from lib2to3.refactor import get_all_fix_names
from tempfile import tempdir
from this import d
from django.db import models
import pandas as pd
import os

# Create your models here.
def nav(type):
    
    url = ['index', 'about', 'product', 'B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR',]
    appTitle = ['JAL', 'About', 'Product', 'ZMH', 'YDJ', 'DDL',]
    
    nav = {
        'About': 'about',
        'Product': 'product',
        'ZMH': 'zmh',
        'YDJ': 'ydj',
        'DDL': 'ddl',
    }

    if type == 'url':
        return url
    elif type == 'appTitle':
        return appTitle
    elif type == 'nav':
        return nav
    else:
        pass

'''
全局变量
'''
asin = ['B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR']
version = ['/v1.00', '/v1.01', '/v1.02']

dataFile_01 = 'static/csv/' +  asin[0] + '.csv'
dataFile_02 = 'static/csv/' +  asin[1] + '.csv'
dataFile_03 = 'static/csv/' +  asin[2] + '.csv'

# listing图片名称数据字典
imgName_Listing = {
        asin[0]: os.listdir('static/image/' + asin[0] + version[0] + '/7'),
        asin[1]: os.listdir('static/image/' + asin[1] + version[0] + '/7'),
        asin[2]: os.listdir('static/image/' + asin[2] + version[0] + '/7'),
    }
# A_plus图片名称数据字典
imgName_A_plus = {
        asin[0]: os.listdir('static/image/' + asin[0] + version[0] + '/a_plus'),
        asin[1]: os.listdir('static/image/' + asin[1] + version[0] + '/a_plus'),
        asin[2]: os.listdir('static/image/' + asin[2] + version[0] + '/a_plus'),
    }
# print(imgName_Listing['B09YLLXKDT'])
# show图片名称数据字典
imgShow = os.listdir('static/image/show')
imgShower = []
for i in range(3):
    imgShower.append('/static/image/show/' + imgShow[i])
print(imgShower)

'''
链接数据库-
'''
def conData(asin):

    if asin == 'B09YLLXKDT':
        data_listing = pd.read_csv(dataFile_01, encoding = 'GBK', engine='python')
    elif asin == 'B09YLKWBMV':
        data_listing = pd.read_csv(dataFile_02, encoding = 'GBK', engine='python')
    elif asin == 'B09KG4R3YR':
        data_listing = pd.read_csv(dataFile_03, encoding = 'GBK', engine='python')
    # print(dataFile)
    
    return data_listing

def listingData(asin):

    '''
    通过asin获取产品listing数据，并以Dict类型返回
    {{ asin.listingImg }}
    {{ asin.ProductTitle }}
    '''

    data_listing = conData(asin)

    temp = []
    for i in range(1,9):
        temp.append(data_listing.iloc[i,1])

    listingData = {
        'listingImg': '/static/image/' + asin + version[0] + '/7/' + imgName_Listing[asin][0],
        'ProductTitle': temp[0],
        'BulletPoint': [temp[1],temp[2],temp[3],temp[4],temp[5]],
        'Description': temp[6],
        'a_plus_img': [1,2,3]
    }

    return listingData, temp[0]
# listingData('B09YLLXKDT')

def productInfo():

    '''
    获取各文件夹下的图片，将图片分类
    '''
    

    img_url = [
        '/static/image/' + asin[0] + version[0] + '/7/' + imgName_Listing[asin[0]][0],
        '/static/image/' + asin[1] + version[0] + '/7/' + imgName_Listing[asin[1]][0],
        '/static/image/' + asin[2] + version[0] + '/7/' + imgName_Listing[asin[2]][0],
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

def showInfo():
    '''
    处理首页及营销页面的图片、文字
    '''
    listingData = {
        'img': 'img',
        'ProductTitle': '',
        'BulletPoint': '',
        'Description': '',
        'a_plus_img': '',
    }