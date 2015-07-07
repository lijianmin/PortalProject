from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext
from django.conf 					import settings

from profile.models                 import User, UserProfile, PublicUserProfile, ClinicianProfile

# Create your views here.
def main(request):

    return render_to_response(
		'docdirectory/doc_profile_2.html',
		RequestContext(request))

def view_doctor_profile(request, doctor_profile_id):

    clinician_profile = get_object_or_404(ClinicianProfile, id=doctor_profile_id)
    user_profile = get_object_or_404(UserProfile, id=clinician_profile.userprofile.id)
    user_details = get_object_or_404(User, id=user_profile.user.id)

    return render_to_response('profile/doc_profile_2.html',
                                {'clinician_profile':clinician_profile,
                                'user_profile':user_profile,
                                'user_details':user_details,},
                                RequestContext(request))
