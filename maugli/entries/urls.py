from django.conf.urls import url
from django.contrib import admin

from .views import NewsView

app_name = 'store'
urlpatterns = [
    url(r'^$', NewsView.as_view()),
]
