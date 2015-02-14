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
from django.forms					import ModelForm

from portal.models 					import post, category, UserProfile
from portal.forms 					import UserForm, UserProfileForm, AdminProfileForm

from django.contrib.auth.models		import User

from PIL 							import Image 	as PImage
from os.path 						import join 	as pjoin

# Create your views here.    
@login_required
def user_admin(request, pk):
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
		'img':img }, 
		RequestContext(request))

def home(request):
	#list of articles in reverse chronological order
	article_list = post.objects.filter(published = True).order_by("timestamp").reverse()

	#categories
	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)

	#paginate the list of articles for elegance
	paginator = Paginator(article_list, 5) #use small number to test
	
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver the first page
		articles = paginator.page(1)
	except EmptyPage:
		#if page is out of the given range, deliver the last page
		articles = paginator.page(paginator.num_pages)
	
	return render(
		request, 
		'index.html', 
		{'articles' : articles, 'categories' : categories, 'health_threats': health_threats})
	

#need unit test case
def view_article(request, slug, id):

	#return post object
	article = get_object_or_404(post, pk = id)

	return render_to_response('view_article.html', {
		#'comments': Comments.objects.filter(pk = comments  ),
		'health_threats' : category.objects.filter(master_category = 1),
		'categories' : category.objects.filter(master_category = 2),
		'same_cat_articles' : post.objects.filter(category = article.category.id),
		'post': article
	}, RequestContext(request))

#need unit test case
def view_category(request, slug, id):
	
	_category = get_object_or_404(category, pk = id)
	
	return render_to_response('view_category.html', {
		'category': _category,
		'health_threats' : category.objects.filter(master_category = 1),
		'categories' : category.objects.filter(master_category = 2),
		'posts': post.objects.filter(category = id, published = True).order_by("timestamp").reverse()
	}, RequestContext(request))

#need unit test case
def view_master_category(request, slug):
	
	master_category_name = get_object_or_404(master_category, master_category_slug = slug)

	return render_to_response('view_master_category.html', {
		'master_category': master_category_name,
		'child_categories': category.objects.filter(master_category = master_category_name)[:10],
	})

#need unit test case
def register(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

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
			'register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'categories' : categories, 'health_threats': health_threats}, 
			RequestContext(request))

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
				return HttpResponseRedirect('/')
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
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/')
