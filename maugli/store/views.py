from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

class CatalogView(TemplateView):
	template_name = "base_catalog.html"
	def get_context_data(self, **kwargs):
		context = super(CatalogView, self).get_context_data(**kwargs)
		context["css_path"] = settings.CSS_PATH
		context["section"] = {
				"title": "Каталог — "+settings.SITE_NAME,
				"style": "",
		}

		return context

