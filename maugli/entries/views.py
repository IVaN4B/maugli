from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from .models import Entry

class NewsView(TemplateView):
	template_name = "base_news.html"
	def get_context_data(self, **kwargs):
		context = super(NewsView, self).get_context_data(**kwargs)
		context["css_path"] = settings.CSS_PATH
		context["section"] = {
				"title": "Новости — "+settings.SITE_NAME,
		}
		context["entries"] = Entry.objects.filter(type=Entry.ARTICLE)

		return context
