from django.http import HttpResponse
from django.conf import settings
from django.http import Http404

from conf.views import BaseView
from .models import Entry
from menu.models import MenuLink

class EntryView(BaseView):
    template_name = "base_entries.html"
    style = "entries.css"
    NEWS_LINK = "/news"

    def set_data(self, context):
        entry_link = self.get_section_link()
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
            self.title = self.content_title = context["entries"][0].title
        else:
            context["entries"] = Entry.objects.order_by("-date", "-id").filter(
                                                        type=Entry.ARTICLE)
            self.title = self.content_title = "Новости"
            self.style = "news.css"

        context = super(EntryView, self).set_data(context)
        return context

    def get(self, *args, **kwargs):
        return self.render_to_response(self.get_context_data(), **kwargs)
