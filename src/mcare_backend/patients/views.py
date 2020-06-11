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
            if self.request.POST:
                # todo handle error when this fails
                user = PatientProfile.objects.get(
                    user=self.request.user
                    )
                # todo handle error when this fails
                group = PatientGroup.objects.get(
                    id=self.request.data['id']
                    )
                user.group_member.add(group)
                user.save()
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
