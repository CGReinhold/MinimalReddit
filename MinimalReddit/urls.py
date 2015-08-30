from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
import os.path

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'MinimalReddit.site.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^r/', 'MinimalReddit.site.views.sub', name='sub'),
	
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

site_media = os.path.join(
	os.path.dirname(__file__), "site", "templates", "static", "css"
)
