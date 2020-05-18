from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from authapp.serializers import CustomUserSerializer


# Create your views here.
@api_view(['POST',])
def customuser_registration_view(request):
    if request.method == 'POST':
        serializer= CustomUserSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user'
            data['email'] = user.email
            data['firstname'] = user.email
            data['lastname'] = user.email
            data['role'] = user.role
        else:
            data = serializer.errors
        return Response(data, status.HTTP_201_CREATED)

