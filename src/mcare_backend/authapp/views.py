from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from authapp.serializers import CustomUserSerializer


from .models import PatientProfile, ExpertProfile


# Create your views here.
@api_view(['POST',])
@permission_classes([AllowAny])
def customuser_registration_view(request):
    if request.method == 'POST':
        serializer= CustomUserSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user'
            data['username'] = user.username
            data['email'] = user.email
            data['firstname'] = user.firstname
            data['lastname'] = user.lastname
            data['role'] = user.role
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data, status.HTTP_201_CREATED)



# This is just a test view for authentication purposes
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "Expert":
        ExpertProfile.objects.create(user=instance)
    elif created and instance.role == "Patient":
        PatientProfile.objects.create(user=instance)