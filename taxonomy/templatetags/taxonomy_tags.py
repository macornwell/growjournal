from django import template
from taxonomy.services import get_taxonomy_name

register = template.Library()

@register.simple_tag
def taxonomy_name(lifeForm, useLatin):
    return get_taxonomy_name(lifeForm, useLatin)


@register.filter
def order_taxonomy(taxonomyList, useLatin):
    if useLatin:
        return sorted(taxonomyList, key=lambda x: x.latin_name)
    else:
        return sorted(taxonomyList, key=lambda x: x.name)

@register.filter
def order_site_inventory(siteInventorylist, useLatin):
    if useLatin:
        return sorted(siteInventorylist, key=lambda x: x.life_form.latin_name)
    else:
        return sorted(siteInventorylist, key=lambda x: x.life_form.name)



