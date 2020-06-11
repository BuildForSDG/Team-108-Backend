from rest_framework import viewsets

from experts.serializers import (
    ExpertClassSerializer,
    CustomUserSerializer,

    )
from experts.models import ExpertClass
from authapp.models import CustomUser as ExpertUser


class ExpertUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Expertprofile instances.
    """

    serializer_class = CustomUserSerializer
    queryset = ExpertUser.objects.filter(role='Expert')


class ExpertClassViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Expertprofile instances.
    """

    serializer_class = ExpertClassSerializer
    queryset = ExpertClass.objects.all()
