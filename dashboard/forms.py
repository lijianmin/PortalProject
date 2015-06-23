from profile.models 			import User, UserProfile, PublicUserProfile
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


class UserForm(BaseModelForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class UserProfileForm(BaseModelForm):

    class Meta:
        model = UserProfile
        fields = ('country','gender','zip_code','birthday','home_address','mobile_no')

class PublicUserProfileForm(BaseModelForm):

    class Meta:
        model = PublicUserProfile
        fields = (  'allergies', 'height', 'weight', )
