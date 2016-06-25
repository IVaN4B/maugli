from django.db import connection
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

from entries.models import Entry
from store.models import Product

class IndexView(TemplateView):
    template_name = "base_index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["entries"] = Entry.objects.filter(
            type=Entry.ARTICLE).order_by("date")[:10];
        context["products"] = Product.objects.all().prefetch_related(
                                                    'title',
                                                    'price',
                              )[:10];
        return context
