from django.contrib import admin
from feedback.models    import Feedback
from django.db 			import models
from django 			import forms

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feedback, FeedbackAdmin)
