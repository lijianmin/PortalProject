from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext

from django.forms					import ModelForm

from portal.models 					import post, category, UserProfile
from portal.forms 					import UserForm, UserProfileForm, AdminProfileForm
from QnA.models						import Question

from django.contrib.auth.models		import User, Group
from django.contrib.auth.decorators import login_required

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
			#imfn = pjoin("/Users/Jianmin/django_projects/healthportal/wassuphealth/media", profile.avatar.name)
			#im = PImage.open(imfn)
			#im.thumbnail((160,160), PImage.ANTIALIAS)
			#im.save(imfn, "JPEG")
	else:
		pf = AdminProfileForm(instance=userinfo)

	if profile.avatar:
		print(profile.avatar)
		img = profile.avatar.name

	print(img)

	return render_to_response(
		'user_admin.html', {
		'categories' : categories,
		'health_threats': health_threats,
		'profile': profile,
		'userinfo': userinfo,
		'pf':pf,
		'img':img,
		'qns':qns },
		RequestContext(request))
