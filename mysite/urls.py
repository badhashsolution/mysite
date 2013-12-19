from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^polls/', include('polls.urls')), # WGG 12/18/2013 wire an index view into URLconf
   url(r'^admin/', include(admin.site.urls)),
)
