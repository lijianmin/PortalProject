from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext

from portal.models 					import post, category
from profile.models 				import User, UserProfile, ClinicianProfile
from registration.forms 			import UserForm, UserProfileForm, PublicUserProfileForm, ClinicalProfileForm, AdminProfileForm

from django.contrib.auth.models		import User, Group

# Create your views here.
#need unit test case
def register_publicuser(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False
	user_group = 'User'

	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# Did the user provide a profile picture?
			# If so, we need to get it from the input form and put it in the UserProfile model.
			#if 'picture' in request.FILES:
			#    profile.picture = request.FILES['picture']

			# Now we save the UserProfile model instance.
			profile.save()

			# Set user group - for this, we set it to 'User'
			g = Group.objects.get(name = user_group)
			g.user_set.add(user)

			# Update our variable to tell the template registration was successful.
			registered = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print(user_form.errors, profile_form.errors)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render_to_response(
			'registration/register_publicuser.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'categories' : categories, 'health_threats': health_threats},
			RequestContext(request))


def register_clinician(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False
	user_group = 'Clinician'

	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		user_profile_form = UserProfileForm(data=request.POST)
		clinical_profile_form = ClinicalProfileForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and clinical_profile_form.is_valid() and user_profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()
			user.set_password(user.password) # hash password
			user.save()

			user_profile = user_profile_form.save(commit=False)
			user_profile.user = user
			user_profile.save()

			# save clinician profile
			clinical_profile = clinical_profile_form.save(commit=False)
			clinical_profile.userprofile = user_profile
			clinical_profile.save()

			# Set user group - for this, we set it to 'User'
			g = Group.objects.get(name = user_group)
			g.user_set.add(user)

			# Update our variable to tell the template registration was successful.
			registered = True

		else:
			print(user_form.errors, user_profile_form.errors, clinical_profile_form.errors)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		user_profile_form = UserProfileForm()
		clinical_profile_form = ClinicalProfileForm()

	# Render the template depending on the context.
	return render_to_response(
			'registration/register_clinician.html',
			{'user_form': user_form, 'user_profile_form': user_profile_form, 'clinical_profile_form': clinical_profile_form, 'registered': registered, 'categories' : categories, 'health_threats': health_threats},
			RequestContext(request))
