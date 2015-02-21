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
from QnA.models						import Question

from QnA.forms 						import QuestionForm

# Create your views here.
# MAIN - list all forums
def main(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	posted = False

	health_threats = category.objects.filter(master_category = 1)
	categories = category.objects.filter(master_category = 2)

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':

		question_form = QuestionForm(data=request.POST)

		if question_form.is_valid():
			
			Question = question_form.save()

			# Update our variable to tell the template registration was successful.
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


def post_question(request):
	
	if request.method == 'POST':
		question = request.POST.get('question', False)
	
	return render(request, 'qna/qna_post.html', { 'question': question })