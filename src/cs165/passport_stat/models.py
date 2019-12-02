from django.db import models
class passport_stat(models.Model):
	passport_status = models.CharField(max_length=30, null=False, unique=True, primary_key=True)
	extra_documents = models.CharField(max_length=100, blank=True)
# Create your models here.
