from django.conf.urls import patterns, include, url
from django.contrib import admin

# urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tonbotman2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#    ("^bestuursmodel/", include("bestuursmodel.urls")),
#)

urlpatterns = [
    # Examples:
    # url(r'^$', 'tonbotman2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bestuursmodel/', include("bestuursmodel.urls")),
]
