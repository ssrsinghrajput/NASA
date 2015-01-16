from django.conf.urls import patterns, include, url

from django.contrib import admin
from NASAROVER import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('NASAROVER.urls')),
)
