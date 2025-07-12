from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def nav_active(context, name, active_class='text-white', base_class='hover:text-blue-800'):
    current = context['request'].resolver_match.url_name
    if current == name:
        return f"{base_class} {active_class}"
    return base_class


@register.filter
def split(value, delimiter=','):
    """Splits a string by delimiter."""
    return value.split(delimiter)
    