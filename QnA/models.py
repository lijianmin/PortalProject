from django.db 						import models
from django_extensions.db.fields 	import UUIDField
from django.contrib.auth.models     import User
from model_utils.fields             import StatusField
from model_utils                    import Choices
import datetime

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

class Question(models.Model):

    question_category = (
        (1, 'Anaethesiology'),
        (2, 'Cardiology'),
        (3, 'Cardiothoracic Surgery'),
        (4, 'Colorectal Surgery'),
        (5, 'Dentistry'),
        (6, 'Dermatology'),
        (7, 'Endocrinology'),
        (8, 'Ear Nose Throat'),
        (9, 'Gastroenterology'),
        (10, 'General Surgery'),
        (11, 'Geriatrics'),
        (12, 'Gynaecology'),
        (13, 'Haematology'),
        (14, 'Hand Surgery'),
        (15, 'Infectious Disease'),
        (16, 'Internal Medicine'),
        (17, 'Oncology'),
        (18, 'Neonatology'),
        (19, 'Neurology'),
        (20, 'Obstetrics'),
        (21, 'Ophthalmology'),
        (22, 'Orthopaedic Surgery'),
        (23, 'Paediatric'),
        (24, 'Paediatric Surgery'),
        (25, 'Plastic Surgery'),
        (26, 'Psychiatry'),
        (27, 'Renal Medicine'),
        (28, 'Respiratory Medicine'),
        (29, 'Rheumatology'),
        (30, 'Urology')
    )

    # to add
    # ========================
    # 1) status of answer
    # 2) category of answer
    # 3) multiple answer field which consists of UUID, PK, doctor, actual answer

    question_UUID = UUIDField(blank=True, null=True)

    question    = models.CharField(max_length = 300)

    posted_by   = models.ForeignKey(User, blank=True, null=True)

    timestamp   = models.DateTimeField(auto_now_add=True)

    qn_clinical_specialty = models.IntegerField(choices = question_category, default=1)

    STATUS = Choices('PENDING','ANSWERED', 'CONCLUDED','ARCHIVED','CANCELLED')
    status = StatusField()

    def __str__(self):
    	return self.question

    def cancelled(self):
        self.timestamp = datetime.datetime.now()
        self.status = self.STATUS.CANCELLED
        super(Question, self).save()

    def submitted(self):
        self.timestamp = datetime.datetime.now()
        self.status = self.STATUS.PENDING
        super(Question, self).save()

    def concluded(self):
        self.timestamp = datetime.datetime.now()
        self.status = self.STATUS.CONCLUDED
        super(Question, self).save()

    def archived(self):
        self.timestamp = datetime.datetime.now()
        self.status = self.STATUS.ARCHIVED
        super(Question, self).save()

    def answered(self):
        self.timestamp = datetime.datetime.now()
        self.status = self.STATUS.ANSWERED
        super(Question, self).save()


class Answer(models.Model):
    answer_UUID = UUIDField(
        blank=True,
        null=True
    )

    answer = models.TextField()

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    question = models.ForeignKey(Question, blank=True, null=True)

    answer_provided_by = models.ForeignKey(User, blank=True, null=True)
