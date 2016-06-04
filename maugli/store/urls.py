from django.conf.urls import url
from django.contrib import admin

from .views import CatalogView

app_name = 'store'
urlpatterns = [
    url(r'^$', CatalogView.as_view(), name="catalog"),
]
