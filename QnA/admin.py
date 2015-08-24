from django.contrib 	import admin
from QnA.models		    import Specialty, Question, Answer
from django.db 			import models
from django 			import forms

class SpecialtyAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
