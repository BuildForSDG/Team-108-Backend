from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


from authapp.models import ExpertProfile


def get_custom_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': 'Patient'},
                                on_delete=models.CASCADE,
                                related_name="patient_profile")
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    message = models.ManyToManyField(
        'Messages', blank=True) # todo limit the messages to he self created ones
    group_member = models.ManyToManyField(
        'PatientGroup', blank=True)
    assigned_experts = models.ManyToManyField(
        ExpertProfile, blank=True)
    list_of_classes = models.ManyToManyField(
        'ExpertClass', blank=True)

    def __str__(self):
        return self.user.username


class ExpertClass(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ForeignKey(
        'PatientProfile', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class PatientGroup(models.Model):
    name = models.CharField(max_length=240, null=True, blank=True, default='General')

    def __str__(self):
        return self.name


class Messages(models.Model):
    message = models.TextField(null=True, blank=True)
    receiver_expert = models.ForeignKey(
        PatientProfile, related_name="receiver_expert", on_delete=models.SET(get_custom_user))
    receiver_group = models.ForeignKey(
        PatientGroup, related_name="receiver_group", on_delete=models.SET_NULL, null=True, blank=True)
    receiver_class = models.ForeignKey(
        ExpertClass, on_delete=models.SET_NULL, null=True, blank=True)

    # write your custom fields for Expert profile from here.
    def __str__(self):
        return self.message
