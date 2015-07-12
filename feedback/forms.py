from feedback.models            import Feedback
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

class FeedbackForm(BaseModelForm):
    class Meta:
        model = Feedback
        fields = ('submitter_name','submitter_email','feedback_text',)
        help_texts = {
            'submitter_name':'e.g. Winston Churchill',
            'submitter_email':'e.g. winston-churchill@email.com',
            'feedback_text':'Feedback in proper',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)
