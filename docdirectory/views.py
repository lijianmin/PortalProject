from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext
from django.conf 					import settings

from portal.models 					import post, category
from profile.models                 import User, UserProfile, ClinicianProfile

def main(request):

    health_threats = category.objects.filter(master_category = 1)
    categories = category.objects.filter(master_category = 2)

    doc_dir = ClinicianProfile.objects.select_related('userprofile__user').filter(userprofile__user__groups = 1)

    return render_to_response(
		'docdirectory/dir_main.html', {
        'doc_dir': doc_dir,
		'categories' : categories,
		'health_threats': health_threats},
		RequestContext(request))
