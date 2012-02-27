from dajaxice.core import dajaxice_autodiscover
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


# Enable the admin.
admin.autodiscover()

# Use dajaxice for ajax stuff.
dajaxice_autodiscover()


urlpatterns = patterns('',
    # Our core app maintains our URLs.
    url(r'^', include('apps.core.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)
