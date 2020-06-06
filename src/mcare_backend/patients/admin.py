from django.contrib import admin
from .models import PatientProfile, PatientGroup, Messages


# Register your models here.


class PatientProfileAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = PatientProfile


admin.site.register(PatientProfile, PatientProfileAdmin)


class PatientGroupAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = PatientGroup


admin.site.register(PatientGroup, PatientGroupAdmin)


class MessagesAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = Messages


admin.site.register(Messages, MessagesAdmin)
