from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag(name='current_time')
def current_time(format_string):
    return datetime.now().strftime(format_string)

