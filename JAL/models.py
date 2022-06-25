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

imgName_Listing = {
        asin[0]: os.listdir('static/image/' + asin[0] + version[0] + '/7'),
        asin[1]: os.listdir('static/image/' + asin[1] + version[0] + '/7'),
        asin[2]: os.listdir('static/image/' + asin[2] + version[0] + '/7'),
    }

imgName_A_plus = {
        asin[0]: os.listdir('static/image/' + asin[0] + version[0] + '/a_plus'),
        asin[1]: os.listdir('static/image/' + asin[1] + version[0] + '/a_plus'),
        asin[2]: os.listdir('static/image/' + asin[2] + version[0] + '/a_plus'),
    }
print(imgName_Listing['B09YLLXKDT'])


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

    key = ['listingImg', 'ProductTitle', 'BulletPoint', 'Description', 'a_plus_img']
    value = [
        '/static/image/' + asin + version[0] + '/7/' + imgName_Listing[asin][0],
        temp[0],
        [temp[1],temp[2],temp[3],temp[4],temp[5]],
        temp[6],
        [1,2,3]
    ]

    listingData = dict(zip(key,value))
    print(value[0])
    return listingData, temp[0]
# listingData('B09YLLXKDT')

def productInfo():

    '''
    获取各文件夹下的图片，将图片分类
    '''
    

    img_url = [
        '/static/image/' + asin[0] + version[0] + '/7/' + os.listdir('static/image/' + asin[0] + version[0] + '/7')[0],
        '/static/image/' + asin[1] + version[0] + '/7/' + os.listdir('static/image/' + asin[1] + version[0] + '/7')[0],
        '/static/image/' + asin[2] + version[0] + '/7/' + os.listdir('static/image/' + asin[2] + version[0] + '/7')[0],
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
    }

    return productInfo
# print(productInfo())

def test(asin):
    '''
    处理listing页面的数据
    通过asin码，获取对应数据
    数据包括：
    [首图、A+图片、产品标题、5点描述、详细描述]
    [7张图、A+图片、产品标题、5点描述、详细描述、A+描述]
    '''
    listingData = {
        'img': 'img',
        'ProductTitle': '',
        'BulletPoint': '',
        'Description': '',
        'a_plus_img': '',
    }