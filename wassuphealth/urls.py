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

    # Forums - landing and main
    url(r'^forums/$','forums.views.forum_pre_landing', name='view_forums'),
    url(r'^forums/index/$', 'forums.views.main', name='forums'),

    # Community Forums
	url(r'^forums/community/(\d+)/$', 'forums.views.forum', name='forum'),
    url(r'^forums/community/thread/(\d+)/$', 'forums.views.show_thread', name='thread'),
    url(r'^forums/community/reply/(\d+)/$', 'forums.views.reply_to_thread', name='reply'),
    url(r'^forums/community/new_thread/(\d+)/$', 'forums.views.new_thread', name='new_thread'),
    url(r'^forums/community/post/(upvote|downvote)/(\d+)/(\d+)/$', 'forums.views.post_vote', name='post_vote'),

    # Doctors Forums
    url(r'^forums/doc/(\d+)/$', 'QnA.views.show_specialty', name='questions_specialty'),
    url(r'^forums/doc/question/get/(\d+)/$', 'QnA.views.show_specialty_question', name='get_question'),
    url(r'^forums/doc/question/(upvote|downvote)/(\d+)/$', 'QnA.views.question_vote', name='question_vote'),
    url(r'^forums/doc/question/save/(\d+)/$', 'QnA.views.new_question', name='save_question'),
    url(r'^forums/doc/question/answer/save/(\d+)/$', 'QnA.views.save_answer', name='save_answer'),

    # Portal
	url(r'^$','portal.views.home', name='home'),
    url(r'^news/$','portal.views.news', name='news'),
    url(r'^tag/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_tagged_under', name='view_tagged'),
    url(r'^tags/$', 'portal.views.view_all_tags', name='view_all_tags'),
	url(r'^mastercategory/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_master_category', name='view_master_category'),
    url(r'^category/(?P<id>\d+)/(?P<slug>[^\.]+)/$', 'portal.views.view_category', name='view_category'),
    url(r'^article/(?P<id>\d+)/(?P<slug>[^\.]+)', 'portal.views.view_article', name='view_article'),
    url(r'^conditions/$', 'portal.views.view_all_conditions', name='conditions'),
    url(r'^conditions/view/(?P<id>\d+)/(?P<slug>[^\.]+)', 'portal.views.view_condition', name='view_condition'),

 	# Registration
    url(r'^register/public/$', 'registration.views.register_publicuser', name='publicuser_registration'),
    url(r'^register/clinician/$', 'registration.views.register_clinician', name='clinician_registration'),
    url(r'^register/confirm/(?P<activation_key>\w+)/', 'registration.views.register_confirm'),
    url(r'^account-activated/$','registration.views.account_activated', name='account-activated'),
    url(r'^activation-timeout/$','registration.views.account_timeout', name='account-timeout'),

    # User Authentication
    url(r'^login-account/$', 'authentication.views.portal_login', name='portal_login'),
    url(r'^login/$', 'authentication.views.user_login', name='login'),
	url(r'^logout/$', 'authentication.views.user_logout', name='logout'),
    url(r'^account-inactive/$','authentication.views.account_inactive', name='account-inactive'),

    # dashboard
    url(r'^dashboard/$', 'dashboard.views.index', name='dashboard_index'),
    url(r'^dashboard/account/$', 'dashboard.views.edit_profile', name='profile'),
    url(r'^dashboard/healthinfo/$', 'dashboard.views.edit_healthinfo', name='healthinfo'),
    url(r'^dashboard/activities/$', 'dashboard.views.view_activities', name='view_activities'),
    url(r'^dashboard/askadoc/save/$', 'dashboard.views.askadoc_save', name='save_doc_form'),
    url(r'^dashboard/commforums/save/$', 'dashboard.views.commforums_save', name='save_comm_form'),
    url(r'^dashboard/professionalinfo/$', 'dashboard.views.edit_clinicianinfo', name='clinicianinfo'),

    # Profile
    url(r'^doctors/view/(\d+)/$', 'profile.views.view_doctor_profile', name='view_doctor'),

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
