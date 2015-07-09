from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext
from django							import template

from django.contrib.auth            import authenticate, login, logout
from profile.models					import User
from django.contrib.auth.decorators import login_required

def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def account_inactive(request):
    return render(
		request,
		'authentication/account_disabled.html')

def portal_login(request):
	return render(request, 'authentication/login.html')

#need unit test case
def user_login(request):
	# Like before, obtain the context for the user's request.
	#context = RequestContext(request)
    login_error = False

	# If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
        user = authenticate(email=email, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
        if user is not None:
			# Is the account active? It could have been disabled.
            if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
                login(request, user)

                return HttpResponseRedirect(reverse("dashboard.views.index"))

            else:
				# An inactive account was used - no logging in!
                return HttpResponseRedirect('/account-inactive/')
        else:
			# Bad login details were provided. So we can't log the user in.
            login_error = True
            return render_to_response('authentication/login.html', add_csrf(request, login_error=login_error))

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
    else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
        return render('index.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):

	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/')
