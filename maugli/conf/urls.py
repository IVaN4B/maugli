from django.conf.urls import include, url
from django.contrib import admin

from .views import IndexView
from entries.views import EntriesView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include("store.urls")),
    url(r'^(?P<entry_link>news)/', EntriesView.as_view(), name="news"),
    url(r'^(?P<entry_link>\S+)/', include("entries.urls"), name="entry"),
]
