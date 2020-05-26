from rest_framework import viewsets
from rest_framework import serializers

from patients.serializers import PatientProfileSerializer
from patients.models import PatientProfile, ExpertClass


# Create your views here.
class PatientProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patientprofile instances.
    """

    serializer_class = PatientProfileSerializer
    queryset = PatientProfile.objects.all()
