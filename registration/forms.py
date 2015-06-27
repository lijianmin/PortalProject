from profile.models 		    import User, UserProfile, ClinicianProfile, PublicUserProfile, Clinic
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

    email = forms.EmailField(widget=forms.TextInput,
                                label="Email Address")

    username = forms.CharField(widget=forms.TextInput,
                                label="Username")

    password = forms.CharField(widget=forms.PasswordInput,
                                label="Password")

    class Meta:
        model = User
        fields = ('email','username','password','last_name','first_name')
        help_texts = {
            'username':'A unique username e.g. Winston Churchill. This will be used as your display name',
            'email':'A valid email address',
        }

class UserProfileForm(BaseModelForm):

    class Meta:
        model = UserProfile
        fields = ('mobile_no','country')
        help_texts = {
            'mobile_no':'A valid mobile number for use with our 2-factor Authentication',
            'country':'Country of origin e.g. Singapore',
        }

class PublicUserProfileForm(BaseModelForm):

    # Available fields: medical_reg_no, registered_date, practice_address,
    # practice_contact_no, practice_country, practice_website,
    # practice_email_add, clinical_specialty, medical_interests, grad_school,
    # grad_year, degree_type, writeup_text

    class Meta:
        model = PublicUserProfile
        fields = ('allergies','height','weight')

class ClinicForm(BaseModelForm):

    class Meta:
        model = Clinic
        fields = ( 'name', )


class ClinicalUserProfileForm(BaseModelForm):

    # Available fields: medical_reg_no, registered_date, practice_address,
    # practice_contact_no, practice_country, practice_website,
    # practice_email_add, clinical_specialty, medical_interests, grad_school,
    # grad_year, degree_type, writeup_text

    class Meta:
        model = ClinicianProfile
        fields = (  'medical_reg_no',       'registered_date',
                    'clinical_specialty',   'grad_school',
                    'grad_year', 'degree_type',)


class ProfileAvatarForm(BaseModelForm):
	class Meta:
		model = UserProfile
		fields = ('avatar',)
