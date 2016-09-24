from django import template
from taxonomy.services import get_taxonomy_name

register = template.Library()

@register.simple_tag
def taxonomy_name(lifeForm, useLatin):
    return get_taxonomy_name(lifeForm, useLatin)


@register.assignment_tag
def order_genus(genusList, useLatin):
    if useLatin:
        return sorted(genusList, key=lambda x: x.latin_name)
    else:
        return sorted(genusList, key=lambda x: x.name)



