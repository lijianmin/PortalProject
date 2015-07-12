from django.shortcuts               import render
from feedback.models                import Feedback
from feedback.forms                 import FeedbackForm
from django.shortcuts 		        import render, render_to_response
from django.core.context_processors import csrf
from django.template 				import RequestContext

# Create your views here.
def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def index(request):

    feedback_form 	= FeedbackForm()

    return render_to_response(
        'feedback/feedback.html',
        add_csrf(request, feedback_form=feedback_form),
        RequestContext(request))

def submit_feedback(request):

    submitted = False

    feedback_form = FeedbackForm(data=request.POST)

    if request.method == 'POST':

        if feedback_form.is_valid():

            f = feedback_form.save(commit=False)
            f.save()
            submitted = True

    return render_to_response(
        'feedback/feedback.html',
        {'submitted':submitted,},
        RequestContext(request))
