from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings

# Create your models here.


EXPERT = 'Expert'
PATIENT = 'Patient'

ROLES = [(EXPERT, 'Expert'), (PATIENT, 'Patient')]


class MyAccountManager (BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password=None):
        if not email:
            raise ValueError("Users must have an email account")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, firstname, lastname, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    role = models.CharField(max_length=10,  choices=ROLES, default=PATIENT)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # We want the user to log in with email
    USERNAME_FIELD = "email"

    # The fields that are compulsory
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @classmethod
    def has_module_perms(cls, app_label):
        return True


class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': 'Patient'},
                                on_delete=models.CASCADE,
                                related_name="patient_profile")

    # your custom fields for Patient model
    def __str__(self):
        return self.user.username


class ExpertProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': 'Expert'},
                                on_delete=models.CASCADE,
                                related_name="expert_profile")

    # write your custom fields for Expert profile from here.
    def __str__(self):
        return self.user.username
