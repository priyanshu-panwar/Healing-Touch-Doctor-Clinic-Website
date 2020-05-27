from django.shortcuts import render
from .forms import AppointmentForm
from .models import Appointment, Gallery
from django.core.mail import send_mail
from clinic.settings import EMAIL_HOST_USER, CLINIC_MAIL

def home(request):
	return render(request, 'core/index.html')

def appointment(request):
	if request.method=='POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			age = form.cleaned_data.get('age')
			sex = form.cleaned_data.get('sex')
			contact = form.cleaned_data.get('contact')
			address = form.cleaned_data.get('address')
			app = Appointment(name=name, age=age, sex=sex, contact=contact, address=address)
			app.save()
			#send mail
			subject = "Appointment"
			message = f"New appointment: Name:{name}, contact:{contact}, address={address}."
			#send_mail(subject,
			#		message,
			#		EMAIL_HOST_USER,
			#		[CLINIC_MAIL,],
			#		fail_silently=False,
			#		)
			return render(request, 'core/booked.html')
	else:
		form = AppointmentForm()
	return render(request, 'core/appointment.html', {'form': form, })

def contact(request):
	pass

def gallery(request):
	gal = Gallery.objects.all()
	return render(request, 'core/gallery.html', {'gal': gal, })


def dentalimplant(request):
	return render(request, 'core/dentalImplant.html')

def treatments(request):
	return render(request, 'core/treatments.html')

def gallery_int(request, pk):
	gal = Gallery.objects.get(id=pk)
	return render(request, 'core/galleryDetail.html', {'g': gal, })