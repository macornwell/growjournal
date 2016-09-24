from django import template
from django.core.urlresolvers import NoReverseMatch, reverse
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from core.utils import get_summary as coreGetSummary

register = template.Library()
@register.simple_tag
def set_selected_option(index, currentOptionValue, selectedValue=None):
    isSelected = False
    if not selectedValue:
        if index == 1:
            isSelected = True
    else:
        if currentOptionValue.lower() == selectedValue.lower():
            isSelected = True
    if isSelected:
        return 'selected'
    return ''

