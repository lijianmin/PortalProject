from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from portal.models import post, category

# Create your views here.
def home(request):
	#posts = post.objects.values('title','timestamp','author','bodytext', 'title_slug')
	posts = post.objects.all()[:10]
	categories = category.objects.all()[:10]
	return render(request, 'index.html', {'posts' : posts, 'categories' : categories})
	
def view_article(request, slug):
	return render_to_response('view_article.html', {
		'categories' : category.objects.all()[:10],
		'post': get_object_or_404(post, title_slug = slug)
	})

def view_category(request, slug):
	category_name = get_object_or_404(category, category_slug = slug)
	return render_to_response('view_category.html', {
		'category': category_name,
		'categories': category.objects.all()[:10],
		'posts': post.objects.filter(category = category_name)
	})
	