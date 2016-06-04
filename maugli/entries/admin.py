from django.contrib import admin

from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'type', 'get_link_list', 'date')

