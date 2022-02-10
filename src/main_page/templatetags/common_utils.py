from django.conf import settings
from django.template import Library


register = Library()


@register.filter
def get(d, key):
    return d.get(key)


@register.filter
def format_phone_number_for_href(phone_number):
    return (
        (phone_number or str(settings.DEFAULT_EMPTY_TEXT_VALUE))
        .replace(' ', '')
        .replace('(', '')
        .replace(')', '')
        .replace('-', '')
    )
