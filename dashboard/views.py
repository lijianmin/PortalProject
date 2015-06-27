from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext
from django.contrib.auth            import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from django.conf 					import settings

from profile.models					import UserProfile
from forums.models					import Forum, Thread, Post
from QnA.models 					import Specialty, Question
from django.contrib.auth.models		import User
from dashboard.forms 				import UserProfileForm, UserForm, PublicUserProfileForm

# Create your views here.

# list all forums
@login_required
def index(request):

    return render(request, 'dashboard/dashboard_overview.html')

@login_required
def view_activities(request):

    user_doc_qns = Question.objects.filter(posted_by=request.user)
    user_forum_posts = Thread.objects.filter(creator=request.user)

    return render(request, 'dashboard/dashboard_activities.html', {'user_qns':user_doc_qns,'user_posts':user_forum_posts, })

@login_required
def edit_profile(request):

    p_user = request.user
    saved = False

    if request.method == 'POST':

        p_user_profile_form = UserProfileForm(request.POST, instance = p_user.userprofile)
        p_user_form = UserForm(request.POST, instance = p_user)
        p_user_healthprofile_form = PublicUserProfileForm(request.POST, instance=p_user.userprofile.publicuserprofile)

        if p_user_profile_form.is_valid() and p_user_form.is_valid() and p_user_healthprofile_form.is_valid():

            profile = p_user_profile_form.save(commit=False) #one insert statement

            if profile:
                profile.save()
                p_user_form.save()
                p_user_healthprofile_form.save()
                saved = True
            else:
                profile.userprofile = p_user
                profile.save()

                return HttpResponseRedirect(reverse("profile", args=[request.user.pk]))

        else:
            print(p_user_profile_form.errors)

    else:
        p_user_profile_form = UserProfileForm(instance = p_user.userprofile)
        p_user_form = UserForm(instance = p_user)
        p_user_healthprofile_form = PublicUserProfileForm(instance=p_user.userprofile.publicuserprofile)

    return render_to_response(
		'dashboard/dashboard_profile.html', {
		'p_user_profile_form': p_user_profile_form,
        'p_user_form':p_user_form,
        'p_user_healthprofile_form':p_user_healthprofile_form,
        'saved':saved },
		RequestContext(request))
