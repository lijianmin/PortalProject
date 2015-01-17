from django.conf.urls 					import patterns, include, url
from django.contrib 					import admin
#from django.contrib.sitemaps.views 		import sitemap
#from portal.sitemap 					import PostSitemap
from portal 							import views

#sitemaps = {
#	'posts': PostSitemap,
#}

#wires of the site
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^robots\.txt$', include('robots.urls')),
    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	url(r'^$', 'portal.views.home', name='home'),
	url(r'^view/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_master_category', name='view_master_category'),
	url(r'^category/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_category', name='view_category'),
	url(r'^article/(?P<id>\d+)/(?P<slug>[^\.]+)', 'portal.views.view_article', name='view_article'),
	url(r'^forums/$', 'portal.views.forums_admin', name='forums'),
	url(r'^register/$', 'portal.views.register', name='registration'),
	url(r'^login/$', 'portal.views.user_login', name='login'),
	url(r'^logout/$', 'portal.views.user_logout', name='logout'),
	url(r'^useradmin/$', 'portal.views.user_admin', name='useradmin'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django.contrib.flatpages.urls')),
    url(r'^PDPA/$', 'flatpage', {'url': '/PDPA/'}, name='PDPA'),
	url(r'^about-wassuphealth/$', 'flatpage', {'url': '/about-wassuphealth/'}, name='about-wassuphealth'),
    url(r'^legal/terms-of-use/$', 'flatpage', {'url': '/legal/terms-of-use'}, name='legal-terms-of-use'),
)
