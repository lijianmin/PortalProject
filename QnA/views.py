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

from portal.models 					import category
from profile.models					import User, UserProfile, ClinicianProfile, PublicUserProfile
from QnA.models						import Question, Answer, Specialty

from QnA.forms 						import QuestionForm, AnswerForm

# tag question to specialty
#	- EITHER choose a subject and load a page which shows all related questions
#	  and post straight from it if logged into the system (which will tag it under that specialty)
#	- OR post from user's dashboard (specialty list)
#	- Need to re-tweak the category model or deployment of tags for questions and articles which is much more efficient than creating categories
# image upload capability for dermatologist analysis
# Front end notification polling
# Appointment system (basic) with capabilities of only sending sms/email to clinic-in-charge (generated automatically)
# Ernest to get back on the workflow for appointment setup which is related to how questions are answered in the system
# private system for doctor and public user but viewable by public
# when answered by a doctor, it can also be posed back to the same doctor

# MAIN
def show_specialty(request, specialty_id):

    title = Specialty.objects.get(pk=specialty_id).title
    qns = Question.objects.filter(status='ANSWERED',specialty_id=specialty_id, private=False).order_by("upvote").reverse()
    question_form = QuestionForm()

    related_specialists = ClinicianProfile.objects.filter(medical_interests__contains = title)

	# Render the template depending on the context.
    return render_to_response(
			'qna/doc_specialty_questions.html',
			add_csrf(request, question_form=question_form, qns=qns, title=title, specialty_id=specialty_id, related_specialists=related_specialists),
			RequestContext(request))


def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def show_specialty_question(request, question_id):

    question 		= get_object_or_404(Question, id=question_id)
    answer 			= Answer.objects.filter(question_id=question_id)

    userprofile         = question.posted_by.userprofile
    publicuserprofile   = get_object_or_404(PublicUserProfile, id=userprofile.publicuserprofile.id)

    specialty 		= Specialty.objects.get(pk=question.specialty_id)
    specialty_title = specialty.title
    specialty_pk 	= specialty.id

    answer_form 	= AnswerForm()

    return render_to_response(
			'qna/doc_question_answers.html',
			add_csrf(request, Question=question, Answer=answer,
            answer_form=answer_form, specialty_title=specialty_title,
            specialty_id=specialty_pk, question_id=question_id,
            publicuserprofile=publicuserprofile),
			RequestContext(request))

@login_required
def new_question(request, specialty_id):

    specialty = get_object_or_404(Specialty, id=specialty_id)
    question_form = QuestionForm(data=request.POST)

    if request.method == 'POST':

        if question_form.is_valid():

            q = question_form.save(commit=False)
            q.specialty_id = specialty.pk
            q.save()

            q.posted_by_id = request.user.pk
            q.save()

    return HttpResponseRedirect(reverse("QnA.views.show_specialty_question", args=[q.pk]))

# for question
@login_required
def question_vote(request, votetype, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if votetype == 'upvote':
        question.upvote += 1
        question.save()
    elif votetype == 'downvote':
        question.downvote -= 1
        question.save()

    return HttpResponseRedirect(reverse('QnA.views.show_specialty_question', args=[question.id]))

"""
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
"""

@login_required
def answer_question(request, pk):
	question = Question.objects.get(pk=pk)
	answer = Answer.objects.filter(question_id=pk)
	action = reverse("QnA.views.save_answer", args=[pk])
	return render_to_response('qna/qna_answer_qn.html', add_csrf(request, action=action, Question=question, Answer=answer))

@login_required
def save_answer(request, question_id):

    question = get_object_or_404(Question, id=question_id)
    answer_form = AnswerForm(data=request.POST)

    if request.method == 'POST':

        if answer_form.is_valid():

            a = answer_form.save(commit=False)
            a.question_id = question.pk
            a.answer_provided_by_id = request.user.pk
            a.save()

            question.answered()
            question.save()

        else:
            print(answer_form.errors)

    return HttpResponseRedirect(reverse('QnA.views.show_specialty_question', args=[question.id]))
