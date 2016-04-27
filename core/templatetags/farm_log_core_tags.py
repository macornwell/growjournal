from django import template
from core.utils import get_summary as coreGetSummary

register = template.Library()

@register.filter
def get_time(dateTime):
    return dateTime.strftime('%H:%m:%S')

@register.filter
def get_summary(fullText):
    return coreGetSummary(fullText, '')
