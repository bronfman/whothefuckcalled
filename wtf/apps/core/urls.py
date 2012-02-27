from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    # Main page of site.
    url(r'^$', direct_to_template, {'template': 'core/index.html'}),
)
