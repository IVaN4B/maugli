from django import template

from store.models import Product

register = template.Library()

@register.inclusion_tag('snippets/product.html', takes_context=True)
def product(context, product, *args, **kwargs):
    return {'product': product }
