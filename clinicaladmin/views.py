from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext

from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from django.forms					import ModelForm

from portal.models 					import post, category, UserProfile
from portal.forms 					import UserForm, UserProfileForm, AdminProfileForm
from QnA.models						import Question

from django.contrib.auth            import authenticate, login, logout
from django.contrib.auth.models		import User, Group
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def main(request):

	qns = Question.objects.all().order_by("timestamp").reverse()

#	health_threats = category.objects.filter(master_category = 1)
#	categories = category.objects.filter(master_category = 2)
	userinfo = User.objects.get(username = request.user)
	profile = UserProfile.objects.get(user_id = request.user.pk)
    
	return render_to_response(
		'clinicaladmin/clinical_admin_main.html', {
		#'categories' : categories,
		#'health_threats': health_threats,
		'profile': profile,
		'userinfo': userinfo,
		'qns':qns },
		RequestContext(request))

# answer questions
