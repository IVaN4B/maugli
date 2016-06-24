from django.contrib import admin

from store.models import Category, Product, TitleColumn, PriceColumn

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(TitleColumn)
admin.site.register(PriceColumn)
