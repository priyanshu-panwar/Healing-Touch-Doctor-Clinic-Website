from django.contrib import admin
from .models import Gender, Patient

#admin.site.register(Gender)
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display = ['name', 'age', 'sex', 'contact', 'date']
	list_filter = ['date', ]
	search_fields = ('name', )