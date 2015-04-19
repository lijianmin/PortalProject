from portal.models 				import UserProfile, ClinicianProfile, PublicUserProfile
from django.contrib.auth.models import User
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
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        help_texts = {
            'Username':'A unique username e.g. Winston Churchill. This will be used as your display name',
            'email':'A valid email address',
        }


class UserProfileForm(BaseModelForm):

    #country = forms.ChoiceField(choices=['Singapore','Malaysia'])

    class Meta:
        model = UserProfile
        fields = ('birthday','mobile_no','country','home_address','zip_code')
        help_texts = {
            'mobile_no':'A valid mobile phone number for use with our 2-factor Authentication',
            'country':'Country of origin e.g. Singapore',
            'home_address':'Your residential/office address. Optional',
            'zip_code':'Zip/Postal code of your address. Optional'
        }


class PublicUserProfileForm(BaseModelForm):

    # Available fields: medical_reg_no, registered_date, practice_address,
    # practice_contact_no, practice_country, practice_website,
    # practice_email_add, clinical_specialty, medical_interests, grad_school,
    # grad_year, degree_type, writeup_text

    class Meta:
        model = PublicUserProfile
        fields = ('allergies','height','weight')


class ClinicalProfileForm(BaseModelForm):

    # Available fields: medical_reg_no, registered_date, practice_address,
    # practice_contact_no, practice_country, practice_website,
    # practice_email_add, clinical_specialty, medical_interests, grad_school,
    # grad_year, degree_type, writeup_text

    class Meta:
        model = ClinicianProfile
        fields = (  'medical_reg_no',       'registered_date',
                            'practice_address',
                    'practice_contact_no',  'practice_country',
                    'clinical_specialty',   'grad_school',
                    'grad_year',            'degree_type',)


class AdminProfileForm(BaseModelForm):
	class Meta:
		model = UserProfile
		fields = ('avatar',)
