from django.conf.urls.defaults import *

import utilities
from avaliacao.tickets.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Tickets application
    url(r'^ticket/', include('avaliacao.tickets.urls')),

    # django-registration views
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', index, name="avaliacao.ticket.index"),

)

from django.conf import settings

if settings.DEBUG:
    # serve static files from develpment server
    from django.views import static

    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )