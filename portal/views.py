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

from PIL 							import Image 	as PImage
from os.path 						import join 	as pjoin

# Create your views here.
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
