from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

from entries.models import Entry
class IndexView(TemplateView):
	template_name = "base_index.html"
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context["css_path"] = settings.CSS_PATH
		context["section"] = {
				"title": settings.SITE_NAME,
				"style": settings.CSS_PATH+"index.css",
		}

		context["entries"] = Entry.objects.filter(
			type=Entry.ARTICLE).order_by("date")[:10];
		return context
