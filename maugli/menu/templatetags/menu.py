from django import template

from menu.models import Menu

register = template.Library()

@register.inclusion_tag('snippets/menu.html', takes_context=True)
def menu(context, name, *args, **kwargs):
    menu = Menu.objects.get(name=name)
    url = '/'
    url_match = context['request'].resolver_match.args
    if url_match:
        url = "/"+url_match[0]
    links = menu.links.order_by("weight").all()
    title = menu.title
    if "title" in kwargs:
        title = kwargs["title"]
    return {'title': title, 'menu': menu, 'links': links, 'url': url }
