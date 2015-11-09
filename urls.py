from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

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

    url(r'^login/$', login, {'template_name': 'jarrbo/login.html'}, name='aanmelden'),
    url(r'^logout/$', logout, {'next_page': '/bestuursmodel'}, name='afmelden'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bestuursmodel/', include("bestuursmodel.urls")),
]
