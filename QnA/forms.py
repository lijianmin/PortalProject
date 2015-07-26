from QnA.models 				import Question, Answer
from django 					import forms

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', '%s')
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field.help_text
                })

class QuestionForm(BaseModelForm):
    class Meta:
        model = Question
        fields = ('question', 'tag_profile', 'private')
        help_texts = {
            'question':'Question to doctor here',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(QuestionForm, self).__init__(*args, **kwargs)

class AnswerForm(BaseModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)
        help_texts = {
            'question':'Your response here',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AnswerForm, self).__init__(*args, **kwargs)
