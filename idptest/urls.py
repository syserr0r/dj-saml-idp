from django.conf.urls import url, include
from django.contrib.auth.views import login
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Example:
    # (r'^idptest/', include('idptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Required for login:
    url(r'^accounts/login/$', login),

    # URLs for the IDP:
    url(r'^idp/', include('saml2idp.urls')),
]
