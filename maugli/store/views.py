from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

class CatalogView(TemplateView):
    template_name = "base_catalog.html"
