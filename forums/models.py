from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from string import join
from settings import MEDIA_ROOT

class Forum(models.Model):
    title = models.CharField(max_length=60)
    def __str__(self):
        return self.title

class Thread(models.Model):
    title 	= 	models.CharField(max_length=60)
    created =	models.DateTimeField(auto_now_add=True)
    creator = 	models.ForeignKey(User, blank=True, null=True)
    forum 	= 	models.ForeignKey(Forum)

    def __str__(self):
        return self.creator + " - " + self.title

class Post(models.Model):
    title 	=	models.CharField(max_length=60)
    created = 	models.DateTimeField(auto_now_add=True)
    creator = 	models.ForeignKey(User, blank=True, null=True)
    thread 	= 	models.ForeignKey(Thread)
    body 	=	models.TextField(max_length=10000)

    def __unicode__(self):
        return "%s - %s - %s" % (self.creator, self.thread, self.title)

    def short(self):
        return "%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))
    short.allow_tags = True