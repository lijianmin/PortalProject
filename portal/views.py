from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext

from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger

from portal.models 					import post, category
from profile.models					import User

from QnA.models						import Question
from taggit.models					import Tag

from QnA.forms 						import QuestionForm

def account_timeout(request):

	#categories
	#health_threats = category.objects.filter(master_category = 1)
	#categories = category.objects.filter(master_category = 2)

	return render(
		request,
		'authentication/account_activation_timeout.html')


def account_inactive(request):

	#categories
	#health_threats = category.objects.filter(master_category = 1)
	#categories = category.objects.filter(master_category = 2)

	return render(
		request,
		'authentication/account_disabled.html')

def account_activated(request):

	#categories
	#health_threats = category.objects.filter(master_category = 1)
	#categories = category.objects.filter(master_category = 2)

	return render(
		request,
		'authentication/account_activated.html')

def forum_pre_landing(request):

	return HttpResponseRedirect('/forums-disclaimer/')

def news(request):

	article_list = post.objects.filter(published = True).order_by("timestamp").reverse()
	paginator = Paginator(article_list, 5)

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
		'portal/news.html',
		{'articles' : articles})


def conditions(request):

	return render(
		request,
		'portal/conditions.html')


# Create your views here.
def home(request):

	#list of articles in reverse chronological order
	article_list = post.objects.filter(published = True).order_by("timestamp").reverse()

	#categories
	#health_threats = category.objects.filter(master_category = 1)
	#categories = category.objects.filter(master_category = 2)

	#paginate the list of articles for elegance
	paginator = Paginator(article_list, 5) #use small number to test

	#question form
	question_form = QuestionForm()

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
		{'articles' : articles, 'question_form': question_form })



def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d


#need unit test case
def view_article(request, slug, id):

	#return post object
	article = get_object_or_404(post, pk = id)
	tags = Tag.objects.filter(post__id = id)

	return render_to_response('portal/article.html', {
		#'health_threats' : category.objects.filter(master_category = 1),
		#'categories' : category.objects.filter(master_category = 2),
		'same_cat_articles' : post.objects.filter(category = article.category.id),
		'post': article,
		'tags': tags
	}, RequestContext(request))

#need unit test case -- render in alphabetical order
def view_all_tags(request):

	return render_to_response('portal/view_tags.html', {
		#'health_threats' : category.objects.filter(master_category = 1),
		#'categories' : category.objects.filter(master_category = 2),
		'all_tags': Tag.objects.all()
	}, RequestContext(request))

#need unit test case
def view_tagged_under(request, slug, id):

	tag = get_object_or_404(Tag, pk = id)

	return render_to_response('portal/tag.html', {
		'tag': tag,
		'health_threats' : category.objects.filter(master_category = 1),
		'categories' : category.objects.filter(master_category = 2),
		'posts': post.objects.filter(tags__id = id).order_by("timestamp").reverse(),
		'all_tags': Tag.objects.all()
	}, RequestContext(request))

#need unit test case
def view_category(request, slug, id):

	category_name = get_object_or_404(category, pk = id)
	question_form = QuestionForm()

	return render_to_response('portal/category.html', {
		'category': category_name,
		#'health_threats' : category.objects.filter(master_category = 1),
		#'categories' : category.objects.filter(master_category = 2),
		'posts': post.objects.filter(category = id, published = True).order_by("timestamp").reverse(),
		'question_form': question_form
	}, RequestContext(request))

#need unit test case
def view_master_category(request, slug):

	master_category_name = get_object_or_404(master_category, master_category_slug = slug)

	return render_to_response('portal/view_master_category.html', {
		'master_category': master_category_name,
		'child_categories': category.objects.filter(master_category = master_category_name)[:10],
	})
