from django import forms

from .models import passport_stat

class passport_stat_form(forms.ModelForm):
	class Meta:
		model = passport_stat
		fields = [
			'passport_status',
			'extra_documents'
		]