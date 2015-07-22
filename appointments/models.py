from django.db                      import models
from django_extensions.db.fields 	import UUIDField
from django.conf                    import settings
from profile.models					import User, UserProfile, PublicUserProfile, ClinicianProfile

# Create your models here.
class Appointment(models.Model):
    user                = models.ForeignKey(UserProfile)
    doctor              = models.ForeignKey(ClinicianProfile)
    created_datetime    = models.DateTimeField(auto_now_add=True)
    booking_datetime    = models.DateTimeField()
    remarks             = models.TextField(default="")
    email_address       = models.EmailField(max_length=254)
    contact_no          = models.CharField(max_length=25)

    #Change to appointment id of format <year><month><day>-000X where X starts from 1
    appointment_UUID    = UUIDField(blank=True, null=True)

    #image upload in future
    #acknowledged
