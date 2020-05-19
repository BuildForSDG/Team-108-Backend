from django.contrib import admin
from .models import CustomUser, PatientProfile, ExpertProfile


class CustomUserAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)


class PatientProfileAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = PatientProfile


admin.site.register(PatientProfile, PatientProfileAdmin)


class ExpertProfileAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = ExpertProfile


admin.site.register(ExpertProfile, ExpertProfileAdmin)