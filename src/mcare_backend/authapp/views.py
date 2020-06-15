from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import (
    AllowAny,
)

from authapp.serializers import (
        CustomUserSerializer,
        MyTokenObtainPairSerializer,
        PatientUserSerializer,
        ExpertUserSerializer
    )

from .models import CustomUser
from patients.models import PatientProfile, PatientGroup
from experts.models import ExpertProfile, ExpertClass


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


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PatientUserViewSet(viewsets.ModelViewSet):
    serializer_class = PatientUserSerializer
    queryset = CustomUser.objects.filter(role='Patient')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        if (action == 'update'):
            # todo handle error when this fails
            user = PatientProfile.objects.get(
                user=self.request.user
            )
            try:
                group = PatientGroup.objects.get(
                    id=self.request.POST.get('group_id', None)
                )
                user.group_member.add(group)
                user.save()
            except ObjectDoesNotExist:
                pass
            try:
                expert = ExpertProfile.objects.get(
                    user__username=self.request.data.get('expert_name', None)
                )
                user.assigned_experts.add(expert)
                expert.assigned_patients.add(user)
                user.save()
            except ObjectDoesNotExist:
                pass
            try:
                active_class = ExpertClass.objects.get(
                    id=self.request.data.get('id', None)
                )
                user.list_of_classes.add(active_class)
                active_class.members.add(user)
                user.save()
                active_class.save()
            except ObjectDoesNotExist:
                pass

        return context


class ExpertUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Expertprofile instances.
    """

    serializer_class = ExpertUserSerializer
    queryset = CustomUser.objects.filter(role='Expert')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        if (action == 'update'):
            # todo handle error when this fails
            user = ExpertProfile.objects.get(
                user=self.request.user
            )
            # if expert is creating a new class
            # get the class title and description fromthe front end
            # then create the class. also add to its profile
            try:
                class_name = self.request.data['class_name']
                class_description = self.request.data['class_description']
                new_class = ExpertClass(
                    name=class_name,
                    description=class_description
                )
                new_class.save()
                user.list_of_classes.add(new_class)
                user.save()
            except ObjectDoesNotExist:
                pass
        return context
