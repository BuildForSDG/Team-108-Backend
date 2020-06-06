from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


from django.dispatch import receiver
from django.db.models.signals import post_save
from experts.models import ExpertProfile
from patients.models import PatientProfile


EXPERT = 'Expert'
PATIENT = 'Patient'




ROLES = [(EXPERT, 'Expert'), (PATIENT, 'Patient')]


class MyAccountManager (BaseUserManager):
    """
    A class that represents my account manager which
    retains order, tracks each time a manager
    instance is created

    Attributes:
        attr1 (str): Description of 'attr1'

    Inheritance:
        BaseUserManager
    """

    def create_user(self, email, username, firstname, lastname, password=None):
        """Creates a user

        Arguments:
            email {str} -- emailof the user
            username {str} -- username of the user
            firstname {str} -- firstname of the user
            lastname {str} -- lastname of the user

        Keyword Arguments:
            password {str} -- password of the user (default: {None})

        Raises:
            ValueError: if there's no email
            ValueError: if there's no username

        Returns:
            object -- returns the user object
        """
        
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
        """Creates superuser, needed for custom user model

        Arguments:
            email {str} -- email of the user
            username {stry} -- username of the user
            firstname {str} -- firstname of the user
            lastname {str} -- lastname of the user
            password {str} -- password of the user
        """

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
    """A class that for creating the custom user

    Arguments:
        AbstractBaseUser {cls} -- Requirements for custom user model

    Returns:
        user -- a custom user
    """

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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """A signal that creates either expert or patient profile
    depending on theinstance.role value

    Arguments:
        sender {cls} -- The model that send the signal
        instance {obj} -- instance of the custom user model
        created {bol} -- returns true if custom user is created
    """

    if created and instance.role == "Expert":
        ExpertProfile.objects.create(user=instance)
    elif created and instance.role == "Patient":
        PatientProfile.objects.create(user=instance)
