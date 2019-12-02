from django.db import models

class passport_holder(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	SEX_CHOICES = [(MALE, 'M'), (FEMALE, 'F')]
	BYBIRTH = 'B'
	BYNATURALIZATION = 'N'
	BYREACQUISITION = 'R'
	BYELECTION = 'E'
	BYLEGISLATION = 'L'
	APC_CHOICES = [(BYBIRTH, "By Birth"),(BYNATURALIZATION, "By Naturalization"),(BYREACQUISITION, "By Re-acquisition"),(BYELECTION, "By Election"),(BYLEGISLATION, "By Legislation")]
	passport_no = models.CharField(max_length=10, primary_key=True)
	applicant_name = models.CharField(max_length=50)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES)
	birthdate = models.DateField(auto_now = False, auto_now_add = False)
	place_of_birth = models.CharField(max_length=50)
	citizenship_acquiring_method = models.CharField(max_length=30, choices=APC_CHOICES)
	preferred_delivery_address = models.CharField(max_length=200)
	contact_number = models.CharField(max_length=15)
	email_address = models.CharField(max_length=50)
	emergency_contact = models.ForeignKey('emergency_contact.emergency_contact',to_field = 'emergency_contact', on_delete=models.CASCADE)
	issuing_authority = models.CharField(max_length=30)
	passport_status = models.ForeignKey('passport_stat.passport_stat',to_field = 'passport_status', on_delete=models.CASCADE) #This is actually supposed to be a foreign key

# Create your models here.
