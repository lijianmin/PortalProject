from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext

from django.forms					import ModelForm
from django.conf 					import settings

from portal.models 					import post, category, UserProfile
from QnA.models						import Question

from django.contrib.auth.models		import User, Group
from django.contrib.auth.decorators import login_required
from useradmin.forms	 			import PublicUserProfileForm
from registration.forms 			import AdminProfileForm

from PIL 							import Image 	as PImage
from os.path 						import join 	as pjoin

# Create your views here.
@login_required
def user_admin(request, pk):

	qns = Question.objects.filter(posted_by_id = request.user).order_by("timestamp").reverse() #not restricted to users yet

	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)

	userinfo = User.objects.get(username = request.user)
	profile = UserProfile.objects.get(user_id = request.user.pk)
	img = None

	if request.method == "POST":
		pf = AdminProfileForm(request.POST, request.FILES, instance=profile)
		print(pf)
		if pf.is_valid():
			pf.save()
			imfn = pjoin('/Applications/MAMP/htdocs/wsh/images/', profile.avatar.name)
			im = PImage.open(imfn)
			im.thumbnail((160,160), PImage.ANTIALIAS)
			im.save(imfn, "JPEG")
	else:
		pf = AdminProfileForm(instance=userinfo)

	if profile.avatar:
		print(profile.avatar)
		img = profile.avatar.name

	print(img)

	return render_to_response(
		'useradmin/user_admin.html', {
		'categories' : categories,
		'health_threats': health_threats,
		'profile': profile,
		'userinfo': userinfo,
		'pf':pf,
		'img':img,
		'qns':qns },
		RequestContext(request))


@login_required
def manage_healthprofile(request):

	p_user = request.user.userprofile
	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)

	if request.method == 'POST':

		p_user_profile_form = PublicUserProfileForm(request.POST, instance = p_user.publicuserprofile)

		if p_user_profile_form.is_valid():

			profile = p_user_profile_form.save(commit=False) #one insert statement

			if profile:
				profile.save()
			else:
				profile.userprofile = p_user
				profile.save()

			return HttpResponseRedirect(reverse("useradmin", args=[request.user.pk]))

		else:

			print(p_user_profile_form.errors)

	else:

		p_user_profile_form = PublicUserProfileForm(instance = p_user.publicuserprofile)

	return render_to_response(
		'useradmin/p_user_profile.html', {
		'categories' : categories,
		'health_threats': health_threats,
		'p_user_profile_form': p_user_profile_form},
		RequestContext(request))
