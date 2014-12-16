from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from portal.models import post, category

# Create your views here.
def home(request):
	#posts = post.objects.values('title','timestamp','author','bodytext', 'title_slug')
	articles = post.objects.all()[:10]
	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)
	return render(request, 'index.html', {'posts' : articles, 'categories' : categories, 'health_threats': health_threats})
	
def view_article(request, slug, id):
	return render_to_response('view_article.html', {
		'health_threats' : category.objects.filter(master_category = 1),
		'categories' : category.objects.filter(master_category = 2),
		'post': get_object_or_404(post, pk = id)
	})

def view_category(request, slug, id):
	
	category_name = get_object_or_404(category, category_slug = slug)
	
	return render_to_response('view_category.html', {
		'category': category_name,
		'health_threats' : category.objects.filter(master_category = 1),
		'categories' : category.objects.filter(master_category = 2),
		'posts': post.objects.filter(pk = id)
	})

def view_master_category(request, slug):
	
	master_category_name = get_object_or_404(master_category, master_category_slug = slug)

	return render_to_response('view_master_category.html', {
		'master_category': master_category_name,
		'child_categories': category.objects.filter(master_category = master_category_name)[:10],
	})