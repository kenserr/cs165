from django import forms

from .models import passport_holder

class passport_holder_form(forms.ModelForm):
	class Meta:
		model = passport_holder
		fields = [
			'passport_no', 
			'applicant_name',
			'sex',
			'birthdate',
			'place_of_birth',
			'citizenship_acquiring_method',
			'preferred_delivery_address',
			'contact_number',
			'email_address',
			'emergency_contact',
			'issuing_authority',
			'passport_status'
		]

	#def clean_passport_no(self, *args, **kwargs):
	#	passport_no = self.cleaned_data.get("passport_no")
	#	if "EC" == passport_no[:2]:
	#		return passport_no
	#	else:
	#		return forms.ValidationError("This is not a valid passport number.")