from django.db import models
import pandas as pd

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

def conData(asin):

    if asin == 'B09YLLXKDT':
        dataFile = 'static/csv/' + asin + '.csv'
    elif asin == 'B09YLKWBMV':
        dataFile = 'static/csv/' + asin + '.csv'
    # print(dataFile)
    data_listing = pd.read_csv(dataFile, encoding = 'GBK', engine='python')

    return data_listing

def listingCon(asin):
    data_listing = conData(asin)

    key = []
    value = []
    for i in range(1,9):
        # listing_Dict = {
        key.append(data_listing.iloc[i,0])
        value.append(data_listing.iloc[i,1])
        # }
    listing_Dict = dict(zip(key,value))
        
    return list(listing_Dict.values())