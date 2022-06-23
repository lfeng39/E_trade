from tempfile import tempdir
from this import d
from django.db import models
import pandas as pd
import os

# Create your models here.
def nav(type):
    
    url = ['index', 'about', 'product', 'B09YLLXKDT', 'B09YLKWBMV', 'ddl',]
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

def test():

    data_listing = pd.read_excel('static/csv/B09YLLXKDT.xlsx', sheet_name='listing')
    # listing_version = pd_listing.iloc[2,1]
    key = data_listing.iloc[1,0]
    # print(key)
    value = data_listing.iloc[1,1]
    key = []
    value = []
    for i in range(1,9):
        # listing_Dict = {
        key.append(data_listing.iloc[i,0])
        value.append(data_listing.iloc[i,1])
        # }
    listing_Dict = dict(zip(key,value))

    return list(listing_Dict.values())
# print(test())

dataFile_01 = 'static/csv/' + 'B09YLLXKDT' + '.csv'
dataFile_02 = 'static/csv/' + 'B09YLKWBMV' + '.csv'
dataFile_03 = 'static/csv/' + 'B09KG4R3YR' + '.csv'
dataFile_04 = 'static/csv/' + 'urls' + '.csv'
# data_listing = pd.read_csv(dataFile_01, encoding = 'GBK', engine='python')
# data_listing = pd.read_csv(dataFile_02, encoding = 'GBK', engine='python')
# data_listing = pd.read_csv(dataFile_03, encoding = 'GBK', engine='python')

def conData(asin):

    if asin == 'B09YLLXKDT':
        data_listing = pd.read_csv(dataFile_01, encoding = 'GBK', engine='python')
    elif asin == 'B09YLKWBMV':
        data_listing = pd.read_csv(dataFile_02, encoding = 'GBK', engine='python')
    elif asin == 'B09KG4R3YR':
        data_listing = pd.read_csv(dataFile_03, encoding = 'GBK', engine='python')
    # print(dataFile)
    
    return data_listing

def getTitle():
    product_title = [
        pd.read_csv(dataFile_01, encoding = 'GBK', engine='python').iloc[1,1],
        pd.read_csv(dataFile_02, encoding = 'GBK', engine='python').iloc[1,1],
        pd.read_csv(dataFile_03, encoding = 'GBK', engine='python').iloc[1,1]
    ]
    print(product_title)
    return product_title

# def getImgURL():
    # xxx = pd.read_csv(dataFile_04, encoding = 'GBK', engine='python')['img_url'].values
    # yyy = '/static/' + xxx + '/test01.png'

    # 类型1：获取 7 文件夹下的第一张图片作为产品页面的首图展示，返回首图列表
    # 类型2：获取 7 、a_plus文件夹下的所有图片，通过ASIN，返回图片列表

    # return yyy
# print(getImgURL())

# def getImgName():

def asinInfo(asin):
    img_url = '/static/image' + asin + '/'

def listingData(asin):

    '''
    通过asin获取产品listing数据，并以Dict类型返回
    '''

    data_listing = conData(asin)

    temp = []
    for i in range(1,9):
        # listing_Dict = {
        temp.append(data_listing.iloc[i,1])
        # }
    # print(temp[6])
    key = ['img', 'ProductTitle', 'BulletPoint', 'Description', 'a_plus_img']
    value = [
                'img',
                temp[0],
                [temp[1],temp[2],temp[3],temp[4],temp[5]],
                temp[6],
                [1,2,3]
            ]

    listingData = dict(zip(key,value))

    return listingData
# listingData('B09YLLXKDT')