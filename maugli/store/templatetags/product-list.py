from django import template

from store.models import Product

register = template.Library()

@register.inclusion_tag('snippets/product-list.html', takes_context=True)
def show_product_list(context, mode="all", *args, **kwargs):
    modes = {
        "all": Product.objects.all().prefetch_related(
                                                'title',
                                                'price',),
        "new": Product.objects.all().prefetch_related(
                                                'title',
                                                'price',)[:10],
    }
    if mode in modes:
        return {'products': modes[mode] }
    return {'products': modes["all"] }
