from django.contrib import admin

from .models import MenuLink, Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'title')

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'menu')

