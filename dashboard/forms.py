from profile.models 			import User, UserProfile, ClinicianProfile, PublicUserProfile
from QnA.models 				import Question
from forums.models              import Thread
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
        fields = ('feedback_text',)
        help_texts = {
            'feedback_text':'Feedback in proper',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)

class UserForm(BaseModelForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class AvatarForm(BaseModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)

class UserProfileForm(BaseModelForm):

    class Meta:
        model = UserProfile
        fields = ('country','gender','zip_code','birthday','home_address','mobile_no')

class PublicUserProfileForm(BaseModelForm):

    class Meta:
        model = PublicUserProfile
        fields = (  'allergies', 'height', 'weight', )

class ClinicianUserProfileForm(BaseModelForm):

    class Meta:
        model = ClinicianProfile
        fields = ('medical_reg_no','registered_date','clinical_specialty',
                    'medical_careergrade','grad_school','grad_year',
                    'degree_type','years_of_practice','medical_interests',
                    'writeup_text','medical_memberships','publications',
                    'affiliations','awards',)

class CommQuestionForm(BaseModelForm):
    class Meta:
        model = Thread
        fields = ('impact_scale','side_effect_scale','manage_cost','diagnosis_duration','medication','experience','forum')
        help_texts = {
            'experience':'E.g. It has been too tiring for me to juggle between work and health and has taken a toll on my mental wellbeing',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CommQuestionForm, self).__init__(*args, **kwargs)

class DocQuestionForm(BaseModelForm):
    class Meta:
        model = Question
        fields = ('question','specialty',)
        help_texts = {
            'question':'Question to doctor here',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DocQuestionForm, self).__init__(*args, **kwargs)
