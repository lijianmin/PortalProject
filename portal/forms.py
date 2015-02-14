from portal.models 				import UserProfile
from django.contrib.auth.models import User
from django 					import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile_no','country','home_address','zip_code')


class AdminProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('avatar',)
