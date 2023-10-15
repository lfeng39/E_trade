from django.contrib import admin
from JAL import models
# from E_trade.E_trade import custom_admin_site



print('>>> this is admin.py <<<')

# Register your models here.
# class ListingAdmin(admin.ModelAdmin):
#     pass

# @admin.register(models.Listing, models.AsinInfo, models.ProductInfo, site=custom_admin_site)
admin.site.register(models.Listing)
admin.site.register(models.AsinInfo)
admin.site.register(models.ProductInfo)
admin.site.register(models.UserAccount)
# admin.site.register(models.ProductDescription)
admin.site.register(models.Image)
admin.site.register(models.SalesStatus)
admin.site.register(models.Cart)
admin.site.register(models.Order)