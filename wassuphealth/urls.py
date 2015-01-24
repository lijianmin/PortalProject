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

    # Discussion Forums
   	url(r'^forums/$', 'forums.views.main', name='forums'),
	url(r'^forum/(\d+)/$', 'forums.views.forum', name='forum'),
	url(r'^thread/(\d+)/$', 'forums.views.thread', name='thread'),
    url(r'^post/(new_thread|reply)/(\d+)/$', 'forums.views.post', name='post'),
    url(r'^reply/(\d+)/$', 'forums.views.reply', name='reply'),
    url(r'^new_thread/(\d+)/$', 'forums.views.new_thread', name='new_thread'),

    # Portal
	url(r'^$', 'portal.views.home', name='home'),
	url(r'^view/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_master_category', name='view_master_category'),
	url(r'^category/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_category', name='view_category'),
	url(r'^article/(?P<id>\d+)/(?P<slug>[^\.]+)', 'portal.views.view_article', name='view_article'),

 	# User Controls
	url(r'^register/$', 'portal.views.register', name='registration'),
	url(r'^login/$', 'portal.views.user_login', name='login'),
	url(r'^logout/$', 'portal.views.user_logout', name='logout'),
	url(r'^useradmin/(\d+)/$', 'portal.views.user_admin', name='useradmin'),
    url(r'^admin/', include(admin.site.urls)),
    
    # Static Pages
    url(r'', include('django.contrib.flatpages.urls')),
    url(r'^PDPA/$', 'flatpage', {'url': '/PDPA/'}, name='PDPA'),
	url(r'^about-wassuphealth/$', 'flatpage', {'url': '/about-wassuphealth/'}, name='about-wassuphealth'),
    url(r'^legal/terms-of-use/$', 'flatpage', {'url': '/legal/terms-of-use'}, name='legal-terms-of-use'),
)
