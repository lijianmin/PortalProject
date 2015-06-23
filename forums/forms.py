from forums.models 				import Thread, Post
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
        model = Thread
        fields = ('impact_scale','side_effect_scale','manage_cost','diagnosis_duration','medication','experience')
        help_texts = {
            'experience':'E.g. It has been too tiring for me to juggle between work and health and has taken a toll on my mental wellbeing',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(QuestionForm, self).__init__(*args, **kwargs)

class ReplyForm(BaseModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        help_text = {
            'body':'Your answer'
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ReplyForm, self).__init__(*args, **kwargs)
