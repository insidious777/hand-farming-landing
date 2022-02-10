import re

from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


def phone_number_validator(phone_number):
    if not bool(re.fullmatch(r'^\+380\d{9}$', phone_number)):
        raise ValidationError(_('Invalid phone number format'), code='invalid_phone_number_format')


def terms_accepted_validator(terms_accepted):
    if not terms_accepted:
        raise ValidationError(_('Terms not accepted'), code='terms_not_accepted')
