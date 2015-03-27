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

from portal.models 					import post, category, UserProfile
from QnA.models						import Question, Answer
from django.contrib.auth.models		import User

from QnA.forms 						import QuestionForm

# MAIN
@login_required
def main(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	posted = False

	#qns = Question.objects.all().order_by("timestamp").reverse()
	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':

		question_form = QuestionForm(data=request.POST, user=request.user)

		if question_form.is_valid():

			Question = question_form.save() #one insert statement

			Question.posted_by = request.user #another update statement

			Question.save()

			posted = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print(question_form.errors)

	else:
		question_form = QuestionForm()

	# Render the template depending on the context.
	return render_to_response(
			'qna/qna_index.html',
			{'question_form': question_form, 'posted': posted, 'categories' : categories, 'health_threats': health_threats},
			RequestContext(request))


def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

@login_required
def get_question(request, pk):
	question = Question.objects.get(pk=pk)
	repost_qn_action = reverse("QnA.views.repost_question", args=[pk])
	conclude_qn_action = reverse("QnA.views.conclude_question", args=[pk])

	try:
		answer = Answer.objects.filter(question_id=pk)
		return render(request, 'qna/qna_post.html',
			add_csrf(request, repost_qn=repost_qn_action, conclude_qn=conclude_qn_action, Question=question, Answer=answer))
	except Answer.DoesNotExist:
		return render(request, 'qna/qna_post.html',
			add_csrf(request, repost_qn=repost_qn_action, conclude_qn=conclude_qn_action, Question=question))

#meant for public user
#@login_required
#def change_question_status(request, ptype, pk):
#    if ptype == 'conclude':

#    elif ptype == 'repost':

#    return HttpResponseRedirect(reverse("useradmin", args=[request.user.pk]))
#

@login_required
def repost_question(request, pk):
	p = request.POST
	question = Question.objects.get(pk=pk)
	question.submitted()
	question.save()

	return HttpResponseRedirect(reverse("useradmin", args=[request.user.pk]))


@login_required
def conclude_question(request, pk):
	p = request.POST
	question = Question.objects.get(pk=pk)
	question.concluded()
	question.save()

	return HttpResponseRedirect(reverse("useradmin", args=[request.user.pk]))


@login_required
def answer_question(request, pk):
	question = Question.objects.get(pk=pk)
	action = reverse("QnA.views.save_answer", args=[pk])
	return render_to_response('qna/qna_answer_qn.html', add_csrf(request, action=action, Question=question))


def save_answer(request, pk):
	p = request.POST
	if p["body"]:
		question = Question.objects.get(pk=pk)
		post = Answer.objects.create(question=question, answer=p["body"], answer_provided_by=request.user)
		question.answered()
		question.save()

	return HttpResponseRedirect(reverse("clinicaladmin"))
