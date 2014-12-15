from django.conf.urls import patterns, include, url
from django.contrib import admin
from portal import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'portal.views.home', name='home'),
	url(r'^portal/viewmaster/(?P<slug>[^\.]+)', 'portal.views.view_master_category', name='view_master_category'),
	url(r'^portal/viewcategory/(?P<slug>[^\.]+)', 'portal.views.view_category', name='view_category'),
	url(r'^portal/viewarticle/(?P<slug>[^\.]+)', 'portal.views.view_article', name='view_article'),
    url(r'^admin/', include(admin.site.urls)),
)
