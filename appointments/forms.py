from appointments.models 	    import Appointment
from django 					import forms

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', '%s')
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field.help_text
                })

"""
class Appointment(models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL)
    doctor              = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_datetime    = models.DateTimeField(auto_now_add=True)
    remarks             = models.TextField(default="")
    email_address       = models.EmailField(max_length=254)
    contact_no          = models.CharField(max_length=25)
    appointment_UUID    = UUIDField(blank=True, null=True)
"""
class AppointmentForm(BaseModelForm):
    class Meta:
        model = Appointment
        fields = ('contact_no','email_address','remarks','booking_datetime',)
        help_texts = {
            'contact_no':'Your home/mobile number for clinic to contact',
            'email_address':'Your email address for a confirmation to be sent to',
            'remarks':'OPTIONAL: Any remarks if required'
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
