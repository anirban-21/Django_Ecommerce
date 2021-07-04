from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):

	first_name = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Enter your first name',
		'class':'form-control'
	}))

	last_name = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Enter your surname',
		'class':'form-control'
	}))

	email = forms.CharField(widget=forms.EmailInput(attrs={
		'placeholder':'Enter a valid email address',
		'class':'form-control'
	}))

	password = forms.CharField(widget=forms.PasswordInput(attrs={
			'placeholder':'Enter a valid password',
			'class':'form-control'
		}))

	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
			'placeholder':'Confirm your password',
			'class': 'form-control'
		}))

	class Meta:
		model = Account
		fields = ['first_name', 'last_name', 'email', 'password']

	
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError('Passwords do not match !')
