from rest_framework import viewsets

from patients.serializers import (
    PatientGroupSerializer,
    MessagesSerializer,
    CustomUserSerializer
)

from patients.models import (
    PatientGroup,
    Messages
)

from authapp.models import CustomUser as PatientUser


class PatientUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patientprofile instances.
    """

    serializer_class = CustomUserSerializer
    queryset = PatientUser.objects.filter(role='Patient')


class PatientGroupViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patientprofile instances.
    """

    serializer_class = PatientGroupSerializer
    queryset = PatientGroup.objects.all()


class MessagesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Messages instances.
    """

    serializer_class = MessagesSerializer
    queryset = Messages.objects.all()
