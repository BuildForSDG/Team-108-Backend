from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny,
)

from authapp.serializers import CustomUserSerializer

from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    """A class to represent the api view for custom user registration

    Arguments:
        viewsets {ModelViewSet} -- A class that provides actions like list,
        create, retrieve, etc
    """

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    http_method_names = ['post']
    permission_classes = [AllowAny]
