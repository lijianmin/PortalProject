from QnA.models 				import Question 
from django 					import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question',)
