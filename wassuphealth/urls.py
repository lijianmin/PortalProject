from django.conf.urls 					import patterns, include, url
from django.contrib 					import admin
from django.conf                        import settings
from django.conf.urls.static            import static

#from django.contrib.sitemaps.views 	import sitemap
#from portal.sitemap 					import PostSitemap
from portal 							import views
from django.contrib.staticfiles.urls    import staticfiles_urlpatterns

#sitemaps = {
#	'posts': PostSitemap,
#}

#wires of the site
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^robots\.txt$', include('robots.urls')),
    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Django-Admin
    url(r'^admin/', include(admin.site.urls)),

    # QnA
    url(r'^questions/$', 'QnA.views.main', name='questions_main'),
    url(r'^questions/post/$', 'QnA.views.post_question', name='questions_post'),

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

 	# Registration
    url(r'^register/$', 'registration.views.register', name='registration'),

    # User Authentication
    url(r'^login/$', 'authentication.views.user_login', name='login'),
	url(r'^logout/$', 'authentication.views.user_logout', name='logout'),

    # User Admin
    url(r'^useradmin/(\d+)/$', 'useradmin.views.user_admin', name='useradmin'),

    # Clinical Admin
    url(r'^clinicaladmin/$', 'clinicaladmin.views.main', name='clinicaladmin'),

    # Static Pages
    url(r'', include('django.contrib.flatpages.urls')),
    url(r'^PDPA/$', 'flatpage', {'url': '/PDPA/'}, name='PDPA'),
	url(r'^about-wassuphealth/$', 'flatpage', {'url': '/about-wassuphealth/'}, name='about-wassuphealth'),
    url(r'^legal/terms-of-use/$', 'flatpage', {'url': '/legal/terms-of-use'}, name='legal-terms-of-use'),

)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        # Media Files
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }),
    )
