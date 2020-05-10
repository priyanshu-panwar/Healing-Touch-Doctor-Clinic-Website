from django.db import models

class Gender(models.Model):
	name = models.CharField(max_length=6, default='')

	def __str__(self):
		return self.name

class Patient(models.Model):
	name = models.CharField(max_length=100, default='')
	age = models.CharField(max_length=2, default='')
	sex = models.OneToOneField(Gender, on_delete=models.CASCADE)
	contact = models.CharField(max_length=13, default='')
	address = models.CharField(max_length=50, default='', blank=True)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		#get_latest_by = ['-date', ]
		ordering = ['-date', ]
		verbose_name_plural = "Patients"

	def __str__(self):
		return self.name

