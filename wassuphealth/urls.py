from django.conf.urls 	import patterns, include, url
from django.contrib 	import admin
from portal 			import views

#wires of the site
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'portal.views.home', name='home'),
	url(r'^view/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_master_category', name='view_master_category'),
	url(r'^category/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_category', name='view_category'),
	url(r'^article/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_article', name='view_article'),
	url(r'^register/$', 'portal.views.register', name='registration'),
    url(r'^admin/', include(admin.site.urls)),
)
