from django.db import models
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import datetime, time
import pandas as pd
import os
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
    def __str__(self):
        return self.asin

class Listing(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    sku = models.CharField(max_length=30, blank=True)
    sku_sn = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=300, blank=True)
    price = models.IntegerField()
    bullet_point = models.TextField(max_length=3000, blank=True)
    description = models.TextField(max_length=3000, blank=True)
    status = models.CharField(max_length=2, blank=True)
    def __str__(self):
        return self.asin + ' *** ' + self.title

class ProductInfo(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    sku = models.CharField(max_length=30, blank=True)
    sku_sn = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=300, blank=True)
    price = models.IntegerField()
    bullet_point = models.CharField(max_length=3000, blank=True)
    description = models.TextField(max_length=500, blank=True)
    first_img = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=2, blank=True)
    def __str__(self):
        return self.asin + ' *** ' + self.title

class ProductDescription(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    bullet_point_00 = models.CharField(max_length=500, blank=True)
    bullet_point_01 = models.CharField(max_length=500, blank=True)
    bullet_point_02 = models.CharField(max_length=500, blank=True)
    bullet_point_03 = models.CharField(max_length=500, blank=True)
    bullet_point_04 = models.CharField(max_length=500, blank=True)
    bullet_point_05 = models.CharField(max_length=500, blank=True)
    bullet_point_06 = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=3000, blank=True)

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



print('>>> this is models.py <<<')

