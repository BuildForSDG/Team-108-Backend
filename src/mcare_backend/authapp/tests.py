from django.test import TestCase
from authapp.models import CustomUser, MyAccountManager

# Create your tests here.
class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(
            email="test@gmail.com", 
            username= "ezekieltech",
            firstname= 'Ezekiel',
            lastname= 'Obha',
            password= 'password'
            )
        # CustomUser.objects.create(name="cat", sound="meow")

    def test_CustomUsers_has_correct_firstname_lastname(self):
        """CustomUsers has the correct firstname and lastname"""
        firstname = CustomUser.objects.get(firstname="Ezekiel")
        lastname = CustomUser.objects.get(lastname="Obha")
        self.assertEqual(firstname.firstname, 'Ezekiel')
        self.assertEqual(lastname.lastname, 'Obha')
    
    def test_CustomUsers_has_correct_number_of_fields_passed_to_it(self):
        """CustomUsers has the correct firstname"""
        number_of_fields = len(CustomUser._meta.concrete_fields)
        self.assertEqual(number_of_fields, 13)
