from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login, authenticate, logout

from authapp.serializers import CustomUserSerializer

from rest_framework.authtoken.models import Token


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
@permission_classes([IsAuthenticated])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})