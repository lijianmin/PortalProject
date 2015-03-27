from QnA.models 				import Question
from django 					import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(QuestionForm, self).__init__(*args, **kwargs)
