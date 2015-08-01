# Community Forums

from django.conf                import settings
from django.db 					import models
from profile.models             import User
from model_utils.fields         import StatusField

class Forum(models.Model):

    title = models.CharField(max_length=60)
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

class Thread(models.Model):
    title 	= 	models.CharField(max_length=60)
    condition_desc 	= 	models.TextField(blank=True, default="")
    created =	models.DateTimeField(auto_now_add=True)
    creator = 	models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    forum 	= 	models.ForeignKey(Forum)
    upvote      =   models.IntegerField(default=0)
    downvote    =   models.IntegerField(default=0)

    # core information fields - setup core lookup tables for common_scale_options, manage_cost_option, diagnosis_duration_option
    common_scale_options = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
    )

    impact_scale = models.IntegerField(choices = common_scale_options, default=1)
    side_effect_scale = models.IntegerField(choices = common_scale_options, default=1)

    manage_cost_option = (
        (1, 'Not Costly'),
        (2, 'Costly'),
        (3, 'Very Costly'),
    )
    manage_cost = models.IntegerField(choices = manage_cost_option, default=1)

    diagnosis_duration_option = (
        (1, '< 1 Year'),
        (2, '2 - 5 Years'),
        (3, '> 5 Years'),
    )
    diagnosis_duration = models.IntegerField(choices = diagnosis_duration_option, default=1)

    medication = models.TextField(default="")
    experience = models.TextField(default="")

    #def __str__(self):
    #    return self.creator + " - " + self.title

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return self.post_set.count() - 1

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created")[0]


class Post(models.Model):
    title 	=	models.CharField(max_length=60)
    created = 	models.DateTimeField(auto_now_add=True)
    creator = 	models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    thread 	= 	models.ForeignKey(Thread)
    body 	=	models.TextField()
    upvote      =  models.IntegerField(default=0)
    downvote    =  models.IntegerField(default=0)

    def __str__(self):
        return "%s - %s - %s" % (self.creator, self.thread, self.title)

    def totalvotes(self):
        return self.upvote + self.downvote

    def short(self):
        return "%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))
    short.allow_tags = True
