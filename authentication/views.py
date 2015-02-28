from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext

from django.contrib.auth            import authenticate, login, logout
from django.contrib.auth.models		import User, Group
from django.contrib.auth.decorators import login_required

#need unit test case
def user_login(request):
	# Like before, obtain the context for the user's request.
	#context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST.get('username', False)
		password = request.POST.get('password', False)

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		print(user)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user is not None:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)

				if user.groups.all() == "User":
					print("User login happened")
					return HttpResponseRedirect('/')
				else:
					print("User login happened")
					return HttpResponseRedirect('/clinicaladmin/')
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your portal account has been disabled. Please contact support.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print ("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render('index.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):

	print("User logout happened")

	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/')