from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from portal.models import posts, category

# Create your views here.
def home(request):
	entries = posts.objects.values('title','timestamp','author')
	categories = category.objects.all()[:10]
	return render(request, 'index.html', {'posts' : entries, 'categories' : categories})
	
#def view_article(request):
