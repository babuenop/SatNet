# inventario/templatetags/filters.py
from django import template

register = template.Library()

@register.filter
def map(queryset, attr):
    """
    Permite hacer algo como: {{ queryset|map:'campo' }}
    También funciona con campos de fecha, ejemplo: map:'fecha|date:\"M Y\"'
    """
    if '|' in attr:
        field, _, fmt = attr.partition('|')
        fmt = fmt.replace('date:\"', '').replace('\"', '')
        return [getattr(obj, field).strftime(fmt) if getattr(obj, field) else '' for obj in queryset]
    return [getattr(obj, attr) for obj in queryset]
