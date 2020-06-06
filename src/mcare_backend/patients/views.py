from rest_framework import viewsets

from patients.serializers import (
    PatientProfileSerializer,
    PatientGroupSerializer,
    MessagesSerializer
)

from patients.models import (
    PatientProfile,
    PatientGroup,
    Messages
)


class PatientProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patientprofile instances.
    """

    serializer_class = PatientProfileSerializer
    queryset = PatientProfile.objects.all()


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
