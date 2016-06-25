from django import template

from menu.models import Menu

register = template.Library()

@register.inclusion_tag('snippets/menu.html', takes_context=True)
def menu(context, name, *args, **kwargs):
    menu = Menu.objects.get(name=name)
    url = '/'
    match = context['request'].resolver_match.kwargs
    if 'entry_link' in match:
        url += match['entry_link']
    links = menu.links.order_by("weight").all()
    title = menu.title
    if "title" in kwargs:
        title = kwargs["title"]
    return {'title': title, 'menu': menu, 'links': links, 'url': url, }
