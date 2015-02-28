from django.db 						import models
from django_extensions.db.fields 	import UUIDField

# Create your models here.

# Overview
# --------------
# This is for the enhanced QnA system for Clinicians, Pharmacists and the general public
# Users will post a question under a relevant specialty. The question will be routed to the specialty clinicians for an answer.
# If a qn has been answered, clinicians will still see the questions but will not be able to reply to it.
# Reroute to pharmacists if needed or users can choose to end the question.
# All questions will be available on the archive for easy reference by both users and clinicians.

# Model
# --------------
# 1 user can have many posts. A specialty can have many posts.
# Clinicians can belong to at most 1 specialty

# Logic
# --------------
# Questions posted to a specialty will cause the application server to notify the clinicians under the category (send notification)
# Once a question has been answered, clinicians will not be able to answer it. If a user is not satisfied with the answer, overriding the lock is available.
# The same question will then be answered
# User has the choice to close the question or else it will be routed to a pharmacist (need clarification)

#class Specialty(models.Model):

#class Answer(models.Model):
#   answer_UUID = UUIDField(blank=True, null=True)
#   answer = models.TextField()
#   timestamp = models.DateTimeField(auto_now_add=True)
#   answering_provided_by = //to some user who is an authorized clinician

class Question(models.Model):

    # to add
    # ========================
    # 1) status of answer
    # 2) category of answer
    # 3) multiple answer field which consists of UUID, PK, doctor, actual answer

    question_UUID = UUIDField(blank=True, null=True)

    question = models.CharField(
    	max_length = 300
    )

    #specialty = //onetoonefield to Specialty
    #answer = onetomanyfield to Answer
    #question_given_by = //to some user who is just a registered public user

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.question
