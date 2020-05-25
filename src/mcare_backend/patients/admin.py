from django.contrib import admin
from .models import PatientProfile

# Register your models here.


class PatientProfileAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = PatientProfile


admin.site.register(PatientProfile, PatientProfileAdmin)
