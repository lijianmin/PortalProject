from django.conf.urls 					import patterns, include, url
from django.contrib 					import admin
from django.conf                        import settings
from django.conf.urls.static            import static
from portal 							import views
from django.contrib.staticfiles.urls    import staticfiles_urlpatterns

#sitemaps = {
#	'posts': PostSitemap,
#}

#wires of the site
urlpatterns = patterns('',
    # Examples:

    # Django-Admin
    url(r'^admin/', include(admin.site.urls), name='django_admin'),
    url(r'^forums/', include('spirit.urls')),

    # Search
    #url(r'^search/$', 'search.views.search_site', name='search_site'),

    # QnA
    url(r'^questions/$', 'QnA.views.main', name='questions_main'),
    url(r'^questions/get/(\d+)/$', 'QnA.views.get_question', name='get_question'),
    url(r'^questions/answer/(\d+)/$', 'QnA.views.answer_question', name='ans_question'),
    url(r'^questions/save/(\d+)/$', 'QnA.views.save_answer', name='save_answer'),
    url(r'^questions/repost/(\d+)/$', 'QnA.views.repost_question', name='repost_question'),
    url(r'^questions/conclude/(\d+)/$', 'QnA.views.conclude_question', name='conclude_question'),

    # Discussion Forums -- might be trashed
   	#url(r'^forums/$', 'forums.views.main', name='forums'),
	#url(r'^forum/(\d+)/$', 'forums.views.forum', name='forum'),
	#url(r'^thread/(\d+)/$', 'forums.views.thread', name='thread'),
    #url(r'^post/(new_thread|reply)/(\d+)/$', 'forums.views.post', name='post'),
    #url(r'^reply/(\d+)/$', 'forums.views.reply', name='reply'),
    #url(r'^new_thread/(\d+)/$', 'forums.views.new_thread', name='new_thread'),

    # Portal
	url(r'^$', 'portal.views.home', name='home'),
    url(r'^news/$','portal.views.news', name='news'),
    url(r'^conditions/$','portal.views.conditions', name='conditions'),
    url(r'^forum/$','portal.views.forum_pre_landing', name='view_forums'),
	url(r'^view/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_master_category', name='view_master_category'),
    url(r'^tag/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_tagged_under', name='view_tagged'),
    url(r'^tags/$', 'portal.views.view_all_tags', name='view_all_tags'),
	url(r'^category/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_category', name='view_category'),
	url(r'^article/(?P<id>\d+)/(?P<slug>[^\.]+)', 'portal.views.view_article', name='view_article'),

 	# Registration
    url(r'^register/public/$', 'registration.views.register_publicuser', name='publicuser_registration'),
    url(r'^register/clinician/$', 'registration.views.register_clinician', name='clinician_registration'),
    url(r'^register/confirm/(?P<activation_key>\w+)/', 'registration.views.register_confirm'),

    url(r'^account-activated/$','portal.views.account_activated', name='account-activated'),
    url(r'^activation-timeout/$','portal.views.account_timeout', name='account-timeout'),

    # User Authentication
    url(r'^login/$', 'authentication.views.user_login', name='login'),
	url(r'^logout/$', 'authentication.views.user_logout', name='logout'),

    url(r'^account-inactive/$','portal.views.account_inactive', name='account-inactive'),

    # User Admin
    url(r'^useradmin/(\d+)/$', 'useradmin.views.user_admin', name='useradmin'),
    url(r'^useradmin/edit/health/$', 'useradmin.views.manage_healthprofile', name='manage_healthprofile'),

    # Clinical Admin
    url(r'^clinicaladmin/$', 'clinicaladmin.views.main', name='clinicaladmin'),
    url(r'^clinicaladmin/edit/$', 'clinicaladmin.views.manage_clinicalprofile', name='manage_profile'),

    # Doctors Directory
    url(r'^lookforadoc/$', 'docdirectory.views.main', name='docdir'),

    # Static Pages
    url(r'', include('django.contrib.flatpages.urls')),
    url(r'^PDPA/$', 'flatpage', {'url': '/PDPA/'}, name='PDPA'),
	url(r'^about-wassuphealth/$', 'flatpage', {'url': '/about-wassuphealth/'}, name='about-wassuphealth'),
    url(r'^legal/terms-of-use/$', 'flatpage', {'url': '/legal/terms-of-use'}, name='legal-terms-of-use'),
    url(r'^forums/disclaimer/$', 'flatpage', {'url': '/forums/disclaimer/'}, name='forums-disclaimer'),

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
