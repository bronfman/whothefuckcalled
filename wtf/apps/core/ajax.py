from dajaxice.decorators import dajaxice_register
from django.utils.simplejson import dumps
from opencnam import Phone


@dajaxice_register
def lookup_cnam(request, phone_number):
    """Lookup caller ID information using opencnam's python API."""
    phone = Phone(phone_number)
    return dumps({'cnam': phone.cnam or ''})
