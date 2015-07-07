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
from portal.models 					import article
from django.contrib.auth.models		import User
from dashboard.forms 				import UserProfileForm, UserForm, PublicUserProfileForm, ClinicianUserProfileForm, DocQuestionForm, CommQuestionForm

# Create your views here.
def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

@login_required
def index(request):

    article_list = article.objects.filter(published = True).order_by("timestamp").reverse()
    doc_question_form = DocQuestionForm()
    comm_question_form = CommQuestionForm()

    return render_to_response(
            'dashboard/dashboard_overview.html',
            add_csrf(request, doc_question_form=doc_question_form, comm_question_form=comm_question_form, articles=article_list),
            RequestContext(request))

@login_required
def askadoc_save(request):

    question_form = DocQuestionForm(data=request.POST)

    if request.method == 'POST':

        if question_form.is_valid():

            q = question_form.save(commit=False)
            q.posted_by_id = request.user.pk
            q.save()

    return HttpResponseRedirect(reverse("QnA.views.show_specialty_question", args=[q.pk]))

@login_required
def commforums_save(request):

    question_form = CommQuestionForm(data=request.POST)

    if request.method == 'POST':

        if question_form.is_valid():

            q = question_form.save(commit=False)
            q.title = ""
            q.creator_id = request.user.pk
            q.save()

    return HttpResponseRedirect(reverse("forums.views.show_thread", args=[q.pk]))

@login_required
def view_activities(request):

    user_doc_qns = Question.objects.filter(posted_by=request.user)
    user_forum_posts = Thread.objects.filter(creator=request.user)

    return render(request, 'dashboard/dashboard_activities.html', {'user_qns':user_doc_qns,'user_posts':user_forum_posts, })

@login_required
def edit_healthinfo(request):

    p_user = request.user
    saved = False

    if request.method == 'POST':

        p_user_healthprofile_form = PublicUserProfileForm(request.POST, instance=p_user.userprofile.publicuserprofile)

        if  p_user_healthprofile_form.is_valid():

            p_user_healthprofile_form.save()
            saved = True

            return HttpResponseRedirect(reverse("healthinfo"))

        else:
            print(p_user_healthprofile_form.errors)

    else:
        p_user_healthprofile_form = PublicUserProfileForm(instance=p_user.userprofile.publicuserprofile)

    return render_to_response(
		'dashboard/dashboard_health_info.html', {
        'p_user_healthprofile_form':p_user_healthprofile_form,
        'saved':saved },
		RequestContext(request))

@login_required
def edit_clinicianinfo(request):

    p_clinician = request.user
    saved = False

    if request.method == 'POST':

        p_clinicianprofile_form = ClinicianUserProfileForm(request.POST, instance=p_clinician.userprofile.clinicianprofile)

        if  p_clinicianprofile_form.is_valid():

            p_clinicianprofile_form.save()
            saved = True

            return HttpResponseRedirect(reverse("clinicianinfo"))

        else:
            print(p_clinicianprofile_form.errors)

    else:
        p_clinicianprofile_form = ClinicianUserProfileForm(instance=p_clinician.userprofile.clinicianprofile)

    return render_to_response(
		'dashboard/dashboard_clinician_info.html', {
        'p_clinicianprofile_form':p_clinicianprofile_form,
        'saved':saved },
		RequestContext(request))

@login_required
def edit_profile(request):

    p_user = request.user
    saved = False

    if request.method == 'POST':

        p_user_profile_form = UserProfileForm(request.POST, instance = p_user.userprofile)
        p_user_form = UserForm(request.POST, instance = p_user)

        if p_user_profile_form.is_valid() and p_user_form.is_valid():

            profile = p_user_profile_form.save(commit=False) #one insert statement

            if profile:
                profile.save()
                p_user_form.save()
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

    return render_to_response(
		'dashboard/dashboard_profile.html', {
		'p_user_profile_form': p_user_profile_form,
        'p_user_form':p_user_form,
        'saved':saved },
		RequestContext(request))
