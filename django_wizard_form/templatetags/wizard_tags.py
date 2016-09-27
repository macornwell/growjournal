from django import template


def get_summary(totalText, summary=None, maxSummarySize=25):
    text = summary
    if not text:
        text = totalText[:maxSummarySize]
        if len(totalText) > maxSummarySize:
            text += '...'
    return text


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

