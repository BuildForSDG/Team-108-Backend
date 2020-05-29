from rest_framework import viewsets

from experts.serializers import ExpertProfileSerializer, ExpertClassSerializer
from experts.models import ExpertProfile, ExpertClass


# Create your views here.
class ExpertProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Expertprofile instances.
    """

    serializer_class = ExpertProfileSerializer
    queryset = ExpertProfile.objects.all()


class ExpertClassViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Expertprofile instances.
    """

    serializer_class = ExpertClassSerializer
    queryset = ExpertClass.objects.all()
