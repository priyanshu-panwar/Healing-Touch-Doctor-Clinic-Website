from django.db import models
from PIL import Image

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

class Gallery(models.Model):
	title = models.CharField(max_length=50, default='')
	image1 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image2 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image3 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image4 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image5 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image6 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image7 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image8 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image9 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image10 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image11 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	image12 = models.ImageField(upload_to='gallery/', null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Gallery"
		ordering = ['-date', ]

	def __str__(self):
		return self.title

class Appointment(models.Model):
	name = models.CharField(max_length=100, default='')
	age = models.CharField(max_length=2, default='')
	sex = models.ForeignKey(Gender, on_delete=models.CASCADE)
	contact = models.CharField(max_length=13, default='')
	address = models.CharField(max_length=50, default='', blank=True)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		#get_latest_by = ['-date', ]
		ordering = ['-date', ]
		verbose_name_plural = "Appointments"

	def __str__(self):
		return self.name

