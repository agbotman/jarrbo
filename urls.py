from django.conf.urls import patterns, include, url
from django.contrib import admin
from jarrbo.views import jarrbo_home

urlpatterns = [
    url(r'^$', jarrbo_home, name='jarrbo_home'),
    url(r'^accounts/', include('jarrbo.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

try:
    from local_urls import local_urlpatterns
    urlpatterns += local_urlpatterns
except:
    pass