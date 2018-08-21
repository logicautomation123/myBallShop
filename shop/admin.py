from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_number', 'name', 'quantity', 'price', 'market_price', 'create_time', 'update_time')
    ordering = ('-create_time',)
admin.site.register(models.Product, ProductAdmin)
