from django.conf.urls import include, url
from django.contrib import admin

from .views import IndexView
from entries.views import EntriesView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include("store.urls")),
    url(r'^news/', EntriesView.as_view(), name="news"),
    url(r'^(\S+)/', include("entries.urls")),
]
