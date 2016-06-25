from django.conf.urls import url
from django.contrib import admin

from .views import EntryView

app_name = "entries"
urlpatterns = [
    url(r'^$', EntryView.as_view()),
]
