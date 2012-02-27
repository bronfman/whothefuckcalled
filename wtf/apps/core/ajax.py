from dajaxice.decorators import dajaxice_register
from django.utils.simplejson import dumps
from opencnam import Phone


@dajaxice_register
def lookup_cnam(request, phone_number):
    """Lookup caller ID information using opencnam's python API."""
    print 'phone_number', phone_number
    phone = Phone(phone_number)
    print 'phone_number.cnam', phone_number.cnam or ''
    return dumps({'cnam': phone.cnam or ''})
