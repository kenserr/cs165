from django import forms

from .models import emergency_contact


class emergency_contact_form(forms.ModelForm):
	class Meta:
		model = emergency_contact
		fields = [
			'emergency_contact',
			'emergency_contact_number'
		]