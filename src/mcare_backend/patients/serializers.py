from rest_framework import serializers
from patients.models import PatientProfile


class PatientProfileSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = PatientProfile
        fields = ('id', 'owner')