from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets

from patients.serializers import (
    PatientGroupSerializer,
    MessagesSerializer,
    CustomUserSerializer
)

from patients.models import (
    PatientGroup,
    Messages,
    PatientProfile
)

from experts.models import ExpertProfile

from authapp.models import CustomUser as PatientUser


class PatientUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patientprofile instances.
    """

    serializer_class = CustomUserSerializer
    queryset = PatientUser.objects.filter(role='Patient')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        if (action == 'update'):
            # todo handle error when this fails
            user = PatientProfile.objects.get(
                user=self.request.user
            )
            if self.request.POST:
                try:
                    group = PatientGroup.objects.get(
                        id=self.request.POST.get('group_id', None)
                    )
                    user.group_member.add(group)
                except ObjectDoesNotExist:
                    pass

                try:
                    expert = ExpertProfile.objects.get(
                        user__username=self.request.POST.get(
                            'expert_name', None
                        )
                    )
                    user.assigned_experts.add(expert)
                    
                except ObjectDoesNotExist:
                    pass  
        return context


class PatientGroupViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patientprofile instances.
    """

    serializer_class = PatientGroupSerializer
    queryset = PatientGroup.objects.all()

    # needed to help with group creation by any user
    # Todo limit to patients only
    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        if (action == 'create'):
            if self.request.POST:
                new_group = PatientGroup(
                    name=self.request.data['name'],
                    description=self.request.data['description']
                    )
                new_group.save()
        return context


class MessagesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Messages instances.
    """

    serializer_class = MessagesSerializer
    queryset = Messages.objects.all()
