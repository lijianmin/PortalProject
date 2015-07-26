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

from profile.models					import UserProfile
from forums.models					import Forum, Thread, Post
from QnA.models 					import Specialty, Question
from django.contrib.auth.models		import User
from forums.forms 					import QuestionForm, ReplyForm


def forum_pre_landing(request):

	return HttpResponseRedirect('/forums-disclaimer/')

def main(request):

    forums = Forum.objects.order_by('title')
    thread_count = len( Thread.objects.all() )
    question_count = len( Question.objects.all() )
    specialties = Specialty.objects.filter(hot_topic=False).order_by('title')
    hot_topics  = Specialty.objects.filter(hot_topic=True).order_by('title')

    return render(request, 'forums/forums_listing.html', {'forums':forums, 'specialties':specialties, 'hot_topics':hot_topics, 'thread_count':thread_count, 'question_count':question_count})

# Cross Site Request Forgery Protection
def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

# Make pagination
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

# Returns a list of threads posted under the forum. Speech bubble style
def forum(request, pk):

    """Listing of threads in a forum."""
    question_form = QuestionForm()
    threads = Thread.objects.filter(forum=pk).order_by("created")
    threads = mk_paginator(request, threads, 20)
    title = Forum.objects.get(pk=pk).title

    return render_to_response("forums/forum_thread_list.html", add_csrf(request, title=title, threads=threads, pk=pk, question_form=question_form), RequestContext(request))

# Returns a list of postings under thread
def show_thread(request, thread_id):

	"""Listing of posts in a thread."""
	reply_form = ReplyForm()
	posts = Post.objects.filter(thread=thread_id).order_by("upvote").reverse()
	posts = mk_paginator(request, posts, 15)
	t = Thread.objects.get(pk=thread_id)

	return render_to_response("forums/forum_thread_post.html", add_csrf(request, posts=posts, pk=thread_id, title=t.title, thread = t,
                                                       forum_pk=t.forum.pk, reply_form=reply_form), RequestContext(request))

def increment_post_counter(request):
    profile = request.user.userprofile
    profile.posts += 1
    profile.save()

# for post
def post_vote(request, votetype, thread_id, post_id):

    thread = get_object_or_404(Thread, pk=thread_id)
    post   = get_object_or_404(Post, pk=post_id)

    if votetype == 'upvote':
        post.upvote += 1
        post.save()
    elif votetype == 'downvote':
        post.downvote -= 1
        post.save()

    return HttpResponseRedirect(reverse('forums.views.show_thread', args=[thread.id]))

# submit to system and redirect to the new thread page
@login_required
def new_thread(request, pk):

    """Start a new thread."""
    forum = get_object_or_404(Forum, id=pk)
    question_form = QuestionForm(data=request.POST)

    if request.method == 'POST':

        if question_form.is_valid():

            q = question_form.save(commit=False)
            q.title = ""
            q.forum_id = forum.pk
            q.creator_id = request.user.pk
            q.save()

    return HttpResponseRedirect(reverse("forums.views.show_thread", args=[q.pk]))

@login_required
# Submit to system and redirect to the existing thread page
def reply_to_thread(request, pk):

    thread = get_object_or_404(Thread, id=pk)
    reply_form = ReplyForm(data=request.POST)

    """Reply to a thread."""
    if request.method == 'POST':

        if reply_form.is_valid():

            r = reply_form.save(commit=False)
            r.thread_id = thread.pk
            r.creator_id = request.user.pk
            r.save()

        else:
            print(reply_form.errors)

    return HttpResponseRedirect(reverse("forums.views.show_thread", args=[thread.pk]) + "?page=last")
