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
from django.conf 					import settings

from portal.models 					import post, category
from profile.models					import UserProfile
from forums.models					import Forum, Thread, Post
from django.contrib.auth.models		import User

# Create your views here.
# MAIN - list all forums
def main(request):
	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)
	forums = Forum.objects.all()
	return render(request, 'forums/list.html', {'categories' : categories, 'health_threats': health_threats, 'forums':forums})

def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items

def forum(request, pk):
    """Listing of threads in a forum."""
    threads = Thread.objects.filter(forum=pk).order_by("-created")
    threads = mk_paginator(request, threads, 20)
    title = Forum.objects.get(pk=pk).title
    return render_to_response("forums/forum.html", add_csrf(request, title=title, threads=threads, pk=pk), RequestContext(request))

def thread(request, pk):
    """Listing of posts in a thread."""
    posts = Post.objects.filter(thread=pk).order_by("created")
    posts = mk_paginator(request, posts, 15)
    t = Thread.objects.get(pk=pk)
    return render_to_response("forums/thread.html", add_csrf(request, posts=posts, pk=pk, title=t.title,
                                                       forum_pk=t.forum.pk), RequestContext(request))

def increment_post_counter(request):
    profile = request.user.userprofile
    profile.posts += 1
    profile.save()

def post(request, ptype, pk):
    """Display a post form."""
    action = reverse("forums.views.%s" % ptype, args=[pk])
    if ptype == 'new_thread':
        title = "Start New Topic"
        subject = ''
    elif ptype == 'reply':
        title = "Reply"
        subject = "Re: " + Thread.objects.get(pk=pk).title

    return render_to_response("forums/post.html", add_csrf(request, subject=subject,
        action=action, title=title))

@login_required
def new_thread(request, pk):
    """Start a new thread."""
    p = request.POST
    if p["subject"] and p["body"]:
        forum = Forum.objects.get(pk=pk)
        thread = Thread.objects.create(forum=forum, title=p["subject"], creator=request.user)
        Post.objects.create(thread=thread, title=p["subject"], body=p["body"], creator=request.user)

    increment_post_counter(request)

    return HttpResponseRedirect(reverse("forums.views.forum", args=[pk]))

@login_required
def reply(request, pk):
    """Reply to a thread."""
    p = request.POST
    if p["body"]:
        thread = Thread.objects.get(pk=pk)
        post = Post.objects.create(thread=thread, title=p["subject"], body=p["body"],
            creator=request.user)

    increment_post_counter(request)

    return HttpResponseRedirect(reverse("forums.views.thread", args=[pk]) + "?page=last")
