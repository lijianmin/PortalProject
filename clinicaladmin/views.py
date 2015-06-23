from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext

from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from django.forms					import ModelForm

from portal.models 					import article, category
from profile.models					import User, UserProfile, ClinicianProfile
from clinicaladmin.forms 			import ClinicalProfileForm
from QnA.models						import Question

from django.contrib.auth            import authenticate, login, logout
from profile.models					import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def main(request):

	qns = Question.objects.filter(status='PENDING').order_by("timestamp").reverse()

	userinfo = User.objects.get(email = request.user)
	profile = UserProfile.objects.get(user_id = request.user.pk)

	# need clinical profile

	return render_to_response(
		'clinicaladmin/clinical_admin_main.html', {
		'profile': profile,
		'userinfo': userinfo,
		'qns':qns },
		RequestContext(request))

# post articles
def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

#def post_article(request):

# edit profile
def manage_clinicalprofile(request):

	c_user = request.user.userprofile.clinicianprofile

	if request.method == 'POST':

		clinical_profile_form = ClinicalProfileForm(request.POST, instance = c_user)
		# another for user...similar to the above

		if clinical_profile_form.is_valid():

			profile = clinical_profile_form.save(commit=False) #one insert statement
			profile.save()

			return HttpResponseRedirect(reverse("clinicaladmin"))

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print(clinical_profile_form.errors)

	else:
		clinical_profile_form = ClinicalProfileForm(instance = c_user)


	# Render the template depending on the context.
	return render_to_response(
			'clinicaladmin/clinician_profile.html', {
			'clinical_profile_form': clinical_profile_form },
			RequestContext(request))
