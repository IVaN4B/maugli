from django.http import HttpResponse
from django.conf import settings
from django.http import Http404

from conf.views import BaseView
from .models import Entry
from menu.models import MenuLink

class EntryView(BaseView):
	template_name = "base_entries.html"
	NEWS_LINK = "/news"
	def get_context_data(self, **kwargs):
		context = super(EntryView, self).get_context_data(**kwargs)
		entry_link = context["section"]["url"]
		context["is_page"] = False
		if entry_link != self.NEWS_LINK:
			links = MenuLink.objects.filter(url=entry_link)
			if not links:
				raise Http404
			first_link = links[0]
			context["is_page"] = True
			context["entries"] = first_link.entry.all()

			if not context["entries"]:
				raise Http404
			self.title = context["entries"][0].title
		else:
			context["entries"] = Entry.objects.filter(type=Entry.ARTICLE)
			self.title = "Новости"
		context["section"]["title"] = self.get_section_title()
		context["section"]["content_title"] = self.title

		return context

	def get(self, *args, **kwargs):
		return self.render_to_response(self.get_context_data(), **kwargs)
