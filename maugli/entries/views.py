from django.http import HttpResponse
from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView

from .models import Entry
from menu.models import MenuLink

# TODO: ListView
class EntriesView(TemplateView):
    template_name = "base_entries.html"
    def get_context_data(self, **kwargs):
        context = super(EntriesView, self).get_context_data(**kwargs)
        context["entries"] = Entry.objects.order_by("-date", "-id").filter(
                                                        type=Entry.ARTICLE)
        return context

class EntryView(TemplateView):
    template_name = "base_entries_entry.html"

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        entry_link = "/"+self.kwargs["entry_link"]
        links = MenuLink.objects.filter(url=entry_link)
        if not links:
            raise Http404
        first_link = links[0]
        entries = first_link.entry.all()
        if not entries:
            raise Http404
        context["entry"] = entries[0]
        return context
