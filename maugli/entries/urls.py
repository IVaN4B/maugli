from django.conf.urls import url
from django.contrib import admin

from .views import EntryView

urlpatterns = [
    url(r'^$', EntryView.as_view()),
]
