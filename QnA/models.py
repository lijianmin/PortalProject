    # Ask a doctor
from django.db 						import models
from django_extensions.db.fields 	import UUIDField
from profile.models                 import User
from model_utils.fields             import StatusField
from model_utils                    import Choices
from django.conf                    import settings

import datetime

class Specialty(models.Model):

    title = models.CharField(max_length=100)

    hot_topic = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def num_posts(self):
        return sum([t.num_posts() for t in self.thread_set.all()])

    def last_post(self):
        if self.thread_set.count():
            last = None
            for t in self.thread_set.all():
                l = t.last_post()
                if l:
                    if not last: last = l
                    elif l.created > last.created: last = l
            return last

    class Meta:
        verbose_name_plural = 'Specialties'

class Question(models.Model):

    """
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
    """

    # to add
    # ========================
    # 1) status of answer
    # 2) category of answer
    # 3) multiple answer field which consists of UUID, PK, doctor, actual answer

    question_UUID = UUIDField(blank=True, null=True)

    private     = models.BooleanField(default=False)

    tag_profile = models.BooleanField(default=False)

    question    = models.TextField()

    posted_by   = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    timestamp   = models.DateTimeField(auto_now_add=True)

    specialty	= models.ForeignKey(Specialty)

    STATUS = Choices('PENDING','ANSWERED', 'CONCLUDED','ARCHIVED','CANCELLED')
    status = StatusField()

    upvote      =   models.IntegerField(default=0)
    downvote    =   models.IntegerField(default=0)

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

    upvote      =   models.IntegerField(default=0)
    downvote    =   models.IntegerField(default=0)

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    question = models.ForeignKey(Question, blank=True, null=True)

    answer_provided_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
