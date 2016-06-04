from django.db import connection
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

from entries.models import Entry

class BaseView(TemplateView):
    CSS_STYLE = "style.css"
    template_name = "base_index.html"
    style = ""
    title = ""
    content_title = ""
    def get_section_title(self):
        if self.title:
            return self.title+" — "+settings.SITE_NAME
        return settings.SITE_NAME

    def get_section_style(self):
        if self.style:
            return settings.CSS_PATH+self.style
        return ""

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context["css_style"] = settings.CSS_PATH+self.CSS_STYLE
        context["info"] = {
                "label": settings.SITE_INFO,
                "social_links": {},
                "author_label": settings.AUTHOR_INFO,
                "author_link": settings.AUTHOR_LINK,
                "connection": connection,
        }
        link_match = self.request.resolver_match.args
        link = "/"
        if link_match:
            link = "/"+link_match[0]

        context["section"] = {
                "title": self.get_section_title(),
                "style": self.get_section_style(),
                "content_title": self.content_title,
                "url": link,
        }
        return context

class IndexView(BaseView):
    template_name = "base_index.html"
    style = "index.css"
    content_title = "Новые поступления"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["entries"] = Entry.objects.filter(
            type=Entry.ARTICLE).order_by("date")[:10];
        return context
