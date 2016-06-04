from django.contrib import admin

from store.models import Category, Column, Product

admin.site.register(Category)
admin.site.register(Column)
admin.site.register(Product)
# Register your models here.
