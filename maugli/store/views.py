from django.http import HttpResponse
from django.conf import settings

from conf.views import BaseView

class CatalogView(BaseView):
    template_name = "base_catalog.html"
    title = "Каталог"
    content_title = "Список игрушек"
