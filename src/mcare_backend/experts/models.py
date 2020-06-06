from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


def get_custom_user():
    """Generates as instance of user

    Returns:
        user -- an instance of the user
    """

    return get_user_model().objects.get_or_create(username='deleted')[0]


class ExpertClass(models.Model):
    """
    A Model Class for holding the expert class

    Attributes:
        attr1 (cls): a generic model class

    Inheritance:
        models.Model

    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ManyToManyField(
        'patients.PatientProfile', blank=True)
    class_modules = models.ManyToManyField('ClassModules', blank=True)

    def __str__(self):
        return self.name


class ClassModules(models.Model):
    """
    A django model that handles the Class Modules

    Attributes:
        attr1 (str): Inherits from generic models

    Inheritance:
        models.Model

    """
    title = models.CharField(max_length=50)
    article = models.TextField()

    def __str__(self):
        return self.title


class ExpertProfile(models.Model):
    """A django model for expert profile

    Arguments:
        models {Generic Model} -- A generic model class
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': 'Expert'},
                                on_delete=models.CASCADE,
                                related_name="expert_profile")
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    message = models.ManyToManyField(
        'patients.Messages', blank=True)
    assigned_patients = models.ManyToManyField(
        'patients.PatientProfile', blank=True)
    list_of_classes = models.ManyToManyField(
        'ExpertClass', blank=True)

    def __str__(self):
        return self.user.username
