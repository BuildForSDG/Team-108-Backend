from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from authapp.models import CustomUser, PatientProfile, ExpertProfile
from .views import create_user_profile


# Create your tests here.
class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(
            email="test@gmail.com", 
            username= "ezekieltech",
            firstname= 'Ezekiel',
            lastname= 'Obha',
            password= 'password',
            role = 'Patient'
            )
        self.create_url = reverse('authapp:register')

    def test_create_user_valid_token(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword',
            'password2': 'somepassword',
            'firstname': 'foo',
            'lastname': 'bar',
            'role': 'Patient'
        }

         # URL for creating an account.
        
        response = self.client.post(self.create_url , data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(CustomUser.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the role and token upon successful creation.
        self.assertEqual(response.data['role'], data['role'])
        self.assertTrue('token' in response.data)
        self.assertFalse('password' in response.data)
        self.assertEqual(PatientProfile.objects.count(), 2)

    def test_CustomUsers_has_correct_firstname_lastname(self):
        """CustomUsers has the correct firstname and lastname"""
        firstname = CustomUser.objects.get(firstname="Ezekiel")
        lastname = CustomUser.objects.get(lastname="Obha")
        role = CustomUser.objects.get(role="Patient")
        self.assertEqual(firstname.firstname, 'Ezekiel')
        self.assertEqual(lastname.lastname, 'Obha')
        self.assertEqual(role.role, 'Patient')
    
    def test_CustomUsers_has_correct_number_of_fields_passed_to_it(self):
        """CustomUsers has the correct firstname"""
        number_of_fields = len(CustomUser._meta.concrete_fields)
        self.assertEqual(number_of_fields, 13)

    
    def test_customuser_registration_view_creates_patientprofile(self):
        """
        Ensure we can create a new patient profile when a new user wit 'patient' role.'
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword',
            'password2': 'somepassword',
            'firstname': 'foo',
            'lastname': 'bar',
            'role': 'Patient'
        }

         # URL for creating an account.
        response = self.client.post(self.create_url , data, format='json')

        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the role and token upon successful creation.
        self.assertEqual(response.data['role'], data['role'])
        self.assertEqual(PatientProfile.objects.count(), 2)

    def test_customuser_registration_view_creates_expertprofile(self):
        """
        Ensure we can create a new patient profile when a new user wit 'patient' role.'
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword',
            'password2': 'somepassword',
            'firstname': 'foo',
            'lastname': 'bar',
            'role': 'Expert'
        }

         # URL for creating an account.
        response = self.client.post(self.create_url , data, format='json')

        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the role and token upon successful creation.
        self.assertEqual(response.data['role'], data['role'])
        self.assertEqual(ExpertProfile.objects.count(), 1)