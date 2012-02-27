from re import sub

from dajaxice.decorators import dajaxice_register
from django.core.cache import cache
from django.utils.simplejson import dumps
from opencnam import Phone


@dajaxice_register
def lookup_cnam(request, phone_number):
    """Lookup caller ID information using opencnam's python API."""
    phone_number = unicode(phone_number)
    phone_number = sub(u'\D', '', phone_number)[-10:]

    # Attempt to grab the caller ID name information from the cache.
    cnam = cache.get(phone_number)

    if not cnam:
        cnam = Phone(phone_number).cnam

        # If we got a result back from opencnam, then attempt to cache the name
        # value for as long as possible (30 days with memcached). This way we
        # can get faster responses and not hammer their free API.
        if cnam:
            cache.set(phone_number, cnam, 60 * 60 * 24 * 15)

    return dumps({'cnam': cnam or ''})
