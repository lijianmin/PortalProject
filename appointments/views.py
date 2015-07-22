from appointments.models            import Appointment
from appointments.forms             import AppointmentForm
from profile.models					import User, UserProfile, ClinicianProfile

from django.shortcuts 				import get_object_or_404, render, render_to_response
from django.http 					import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers 		import reverse
from django.views 					import generic
from django.utils 					import timezone
from django.core.context_processors import csrf
from django.template 				import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
save appointment
display appointment form
send email to doctor and user
"""

def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def book_appointment(request, doctor_id):

    doctor_details = get_object_or_404(ClinicianProfile, id=doctor_id)
    doctor_user_details = get_object_or_404(User, id=doctor_details.userprofile.user.id)
    appt_form 	= AppointmentForm()

    return render_to_response(
        'appointments/appointment.html',
        add_csrf(request, appt_form=appt_form, doctor_id=doctor_id, doctor=doctor_details, doctor_user=doctor_user_details),
        RequestContext(request))

@login_required
def save_appointment(request, doctor_id):

    doctor_details = get_object_or_404(ClinicianProfile, id=doctor_id)
    appt_form = AppointmentForm(data=request.POST)
    booked = False

    if request.method == 'POST':

        if appt_form.is_valid():

            appt = appt_form.save(commit=False)
            appt.doctor_id = doctor_details.pk
            appt.user_id = request.user.userprofile.pk
            appt.save()

        else:
            print(appt_form.errors)

    return render_to_response('appointments/appointment_confirmation.html', {'appt':appt,'doctor':doctor_details,}, RequestContext(request))

@login_required
def get_all_appointments(request):

    return render("get all appointments")

@login_required
def delete_appointment(request):

    return render("delete appointment")

@login_required
def edit_appointment(request):

    return render("edit appointment")
