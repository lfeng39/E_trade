from django.db import models
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import datetime, time
from django.utils import timezone
import os
# import djmoney

'''
Create MySQL DB Table
'''
class UserAccount(models.Model):
    user_id = models.CharField(max_length = 20, blank=True)
    user_name = models.CharField(max_length = 20, blank=True)
    email = models.EmailField(max_length = 30, blank=False) # false：必填
    password = models.CharField(max_length = 20, blank=False)
    email_platform = models.EmailField(max_length = 30, blank=True)
    first_name = models.CharField(max_length = 20, blank=True)
    last_name = models.CharField(max_length = 20, blank=True)
    address = models.CharField(max_length = 300, blank=True)
    street = models.CharField(max_length = 300, blank=True)
    city = models.CharField(max_length = 20, blank=True)
    country = models.CharField(max_length = 20, blank=True)
    code = models.CharField(max_length = 20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AsinInfo(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    sku = models.CharField(max_length=30, blank=True)
    sku_sn = models.CharField(max_length=50, blank=True)
    # def __str__(self):
    #     return self.asin

class Listing(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    sku = models.CharField(max_length=30, blank=True)
    sku_sn = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=300, blank=True)
    # price = models.MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bullet_point = models.TextField(max_length=3000, blank=True)
    description = models.TextField(max_length=3000, blank=True)
    first_img = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # date = models.DateTimeField()
    # def __str__(self):
    #     return self.asin + ' *** ' + self.title

class ProductInfo(models.Model):
    asin = models.CharField(max_length=20, blank=True)
    sku = models.CharField(max_length=30, blank=True)
    sku_sn = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=300, blank=True)
    price = models.FloatField()
    bullet_point = models.CharField(max_length=3000, blank=True)
    description = models.TextField(max_length=500, blank=True)
    first_img = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=2, blank=True)
    # def __str__(self):
    #     return self.asin + ' *** ' + self.title

class ProductDescription(models.Model):
    # id = models.CharField(max_length=20, primary_key=True)
    asin = models.CharField(max_length=20, blank=True)
    bullet_point_01 = models.CharField(max_length=500, blank=True)
    bullet_point_02 = models.CharField(max_length=500, blank=True)
    bullet_point_03 = models.CharField(max_length=500, blank=True)
    url = models.CharField(max_length=500, blank=True)

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
    user_id = models.CharField(max_length = 20, blank=True)
    asin = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    order_id = models.CharField(max_length = 20, blank=True)
    user_id = models.CharField(max_length = 20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Coupon(models.Model):
    asin = models.CharField(max_length=1000, blank=True)
    sku = models.CharField(max_length=1000, blank=True)
    title = models.CharField(max_length = 20, blank=True)
    coupon_code = models.CharField(max_length = 20, blank=False)
    type_cash = models.DecimalField(max_digits=10, decimal_places=2)
    type_percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(auto_now_add=True)
    type_status = models.CharField(max_length=2, blank=True)



print('>>> this is models.py <<<')

