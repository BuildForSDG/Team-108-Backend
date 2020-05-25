from rest_framework import viewsets

from patients.serializers import PatientProfileSerializer
from patients.models import PatientProfile


# Create your views here.
class PatientProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patientprofile instances.
    """
    serializer_class = PatientProfileSerializer
    queryset = PatientProfile.objects.all()
