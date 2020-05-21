from django.contrib import admin
from .models import Gender, Patient, Appointment, Gallery

#admin.site.register(Gender)
admin.site.register(Gallery)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display = ['name', 'age', 'sex', 'contact', 'date']
	list_filter = ['date', ]
	search_fields = ('name', )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ['name', 'age', 'sex', 'contact', 'date']
	list_filter = ['date', ]
	search_fields = ('name', )
