from django.db import models
class emergency_contact(models.Model):
	emergency_contact = models.CharField(max_length=50, null=False, unique=True, primary_key=True)
	emergency_contact_number = models.CharField(max_length=15)

# Create your models here.
