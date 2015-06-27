from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext

from profile.models 				import User, UserProfile, ClinicianProfile, PublicUserProfile
from registration.forms 			import UserForm, UserProfileForm, PublicUserProfileForm, ClinicalUserProfileForm, ClinicForm
from django.contrib.auth.models		import Group

from django.core.mail 				import send_mail

from django.conf					import settings

import hashlib, datetime, random

def account_timeout(request):
    return render(
		request,
		'registration/account_activation_timeout.html')

def account_activated(request):
    return render(
		request,
		'registration/account_activated.html')

def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
	if request.user.is_authenticated():
		HttpResponseRedirect('/')

    # check if there is UserProfile which matches the activation key (if not then display 404)
	user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

	#check if the activation key has expired, if it hase then render confirm_expired.html
	if user_profile.key_expires < timezone.now():
    	#return render_to_response('user_profile/confirm_expired.html')
		return HttpResponseRedirect('/account-timeout/')

	#if the key hasn't expired save user and set him as active and render some template to confirm activation
	user = user_profile.user
	user.is_active = True
	user.save()
	#return render_to_response('user_profile/confirm.html')
	return HttpResponseRedirect('/account-activated/')

def emailnotify(usertype, username, email_address, activation_key):

	if usertype == "clinicianuser":
		email_subject = '[TEST] Clinician Account Signup'
		email_body = "There is a new account registered into the system. Username: %s Email Address: %s" % (username, email_address)

		send_mail(email_subject, email_body, 'signup@wassuphealth.com',
			[settings.NOTIFY_EMAIL], fail_silently=True)

	elif usertype == "publicuser":
		email_subject = '[TEST] Next Step to a Great Health: Activation of Your Account'
		email_body = "Hey %s, thanks for signing up. To activate your account, click this link within\
            48hours http://127.0.0.1:8000/register/confirm/%s/" % (username, activation_key)

		send_mail(email_subject, email_body, 'signup@wassuphealth.com',
			[email_address], fail_silently=True)

# Create your views here.
# Need unit test case
def register_publicuser(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False
	user_group = 'User'

	args = {}
	args.update(csrf(request))

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		user_profile_form = UserProfileForm(data=request.POST)
		args['user_form'] = user_form

		# If the two forms are valid...
		if user_form.is_valid() and user_profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			username = user_form.cleaned_data['username']
			email = user_form.cleaned_data['email']
			user.set_password(user.password)
			user.is_active = False
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = user_profile_form.save(commit=False)
			profile.user = user

			# Generate activation key
			salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
			activation_key = hashlib.sha1((salt+email).encode('utf-8')).hexdigest()
			key_expires = datetime.datetime.today() + datetime.timedelta(2)

			profile = UserProfile(user=user, activation_key=activation_key, key_expires=key_expires)
			# Now we save the UserProfile model instance.
			profile.save()

			# Set user group - for this, we set it to 'User'
			g = Group.objects.get(name = user_group)
			g.user_set.add(user)

			#Empty public user profile
			publicprofile = PublicUserProfile(userprofile = profile, allergies = "", height = 0, weight = 0)
			publicprofile.save()

			# Update our variable to tell the template registration was successful.
			registered = True

			emailnotify("publicuser", username, email, activation_key)

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print(user_form.errors, user_profile_form.errors)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		user_profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render_to_response(
			'registration/public-signup.html',
			{'user_form': user_form, 'user_profile_form': user_profile_form, 'registered': registered},
			RequestContext(request))


def register_clinician(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False
	user_group = 'Clinician'

	args = {}
	args.update(csrf(request))

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		user_profile_form = UserProfileForm(data=request.POST)
		clinical_profile_form = ClinicalUserProfileForm(data=request.POST)
		clinic_form = ClinicForm(data=request.POST)
		args['user_form'] = user_form

		# If the two forms are valid...
		if user_form.is_valid() and clinical_profile_form.is_valid() and clinic_form.is_valid() and user_profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()
			username = user_form.cleaned_data['username']
			email = user_form.cleaned_data['email']
			user.set_password(user.password) # hash password
			user.is_active = False
			user.save()

			user_profile = user_profile_form.save(commit=False)
			user_profile.user = user
			user_profile.save()

			# save clinician profile
			clinical_profile = clinical_profile_form.save(commit=False)
			clinical_profile.userprofile = user_profile
			clinical_profile.save()

			# save clinic - need to check if user inputted the text himself/herself
			clinic = clinic_form.save(commit=False)
			clinical_profile.clinic_of_practice = clinic
			clinic.save()

			# Set user group - for this, we set it to 'User'
			g = Group.objects.get(name = user_group)
			g.user_set.add(user)

			# Update our variable to tell the template registration was successful.
			registered = True

			emailnotify("clinicianuser", username, email, "")

		else:
			print(user_form.errors, user_profile_form.errors, clinic_form.errors, clinical_profile_form.errors)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		user_profile_form = UserProfileForm()
		clinical_profile_form = ClinicalUserProfileForm()
		clinic_form = ClinicForm()

	# Render the template depending on the context.
	return render_to_response(
			'registration/doctor-signup.html',
			{'user_form': user_form, 'user_profile_form': user_profile_form, 'clinical_profile_form': clinical_profile_form, 'clinic_form': clinic_form, 'registered': registered},
			RequestContext(request))
