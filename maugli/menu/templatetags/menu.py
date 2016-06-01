from django import template

from menu.models import Menu

register = template.Library()

@register.inclusion_tag('snippets/menu.html')
def menu(name, *args, **kwargs):
	menu = Menu.objects.get(name=name)
	links = menu.links.all()
	title = ""
	if "title" in kwargs:
		title = kwargs["title"]
	return {'title': title, 'menu': menu, 'links': links }
