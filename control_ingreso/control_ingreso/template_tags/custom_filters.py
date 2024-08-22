from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def time_difference(value):
    if value:
        total_seconds = int(value.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}"
    return "N/A"
