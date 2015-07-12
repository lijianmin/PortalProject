from django.db import models

# Create your models here.
class Feedback(models.Model):
    submitter_name = models.CharField(max_length = 120)
    submit_datetime = models.DateTimeField(auto_now_add=True)
    submitter_email = models.CharField(max_length = 120)
    feedback_text = models.TextField(default = "")
