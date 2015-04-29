from profile.models 		    import User, UserProfile, ClinicianProfile
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


class ClinicalProfileForm(BaseModelForm):

    # Available fields: medical_reg_no, registered_date, practice_address,
    # practice_contact_no, practice_country, practice_website,
    # practice_email_add, clinical_specialty, medical_interests, grad_school,
    # grad_year, degree_type, writeup_text

    class Meta:
        model = ClinicianProfile
        fields = (  'medical_reg_no',       'registered_date',
                    'practice_address',     'practice_website',
                    'practice_contact_no',  'practice_country',
                    'practice_email_add',
                    'clinical_specialty',   'grad_school',
                    'grad_year',            'degree_type',
                    'medical_interests',    'writeup_text', )
