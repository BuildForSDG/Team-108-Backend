from django.db import models

from django.conf import settings


# Create your models here.
class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': 'Patient'},
                                on_delete=models.CASCADE,
                                related_name="patient_profile")

    # your custom fields for Patient model
    def __str__(self):
        return self.user.username
