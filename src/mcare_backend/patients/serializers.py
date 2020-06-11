import jsons

from rest_framework import serializers

from patients.models import PatientProfile, Messages, PatientGroup
from experts.models import ExpertProfile, ExpertClass
from authapp.models import CustomUser


'''
This RelatedField classes allows the flexibility of the model
in the response object.
By default, the pk is displayed in the post or get request. By defining this
class, we can specify how we want the message to be represented in the
reponse
reference:
https://stackoverflow.com/questions/55161052/instead-of-primary-key-send-different-field-in-django-rest-framework
'''


class PatientGroupRelatedField(serializers.RelatedField):

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return PatientGroup.objects.get(name=data)


class ExpertProfileRelatedField(serializers.RelatedField):

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return ExpertProfile.objects.get(name=data)


class ExpertClassRelatedField(serializers.RelatedField):

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return ExpertClass.objects.get(name=data)


class PatientProfileSerializer(serializers.ModelSerializer):

    group_member = PatientGroupRelatedField(
        queryset=PatientGroup.objects.all(),
        many=True
    )

    assigned_experts = ExpertProfileRelatedField(
        queryset=ExpertProfile.objects.all(),
        many=True
    )

    list_of_classes = ExpertClassRelatedField(
        queryset=ExpertClass.objects.all(),
        many=True
    )

    message = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = PatientProfile
        fields = [
            'assigned_experts',
            'list_of_classes',
            'message',
            'group_member'
            ]


class CustomUserSerializer(serializers.ModelSerializer):
    """A nexted custom user serializer class. Expertprofile
    serializer is nested in it

    Arguments:
        serializers {ModelSerializer} -- serializes according to the
        custom user model
    """

    patient_profile = PatientProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'firstname',
            'lastname',
            'email',
            'patient_profile'
            ]


class PatientGroupSerializer(serializers.ModelSerializer):

    group_messages = serializers.SerializerMethodField()

    def get_group_messages(self, PatientGroup):
        group_messages = Messages.objects.filter(
            receiver_group_id__name=PatientGroup.name).values(
            'author__username', 'message')
        group_messages_to_json = jsons.dump(
            group_messages)  # gets the queryset serlizable
        return group_messages_to_json

    group_members = serializers.SerializerMethodField()

    def get_group_members(self, PatientGroup):
        group_members = PatientProfile.objects.filter(
            group_member__name=PatientGroup.name).values(
                'user__username'
        )
        group_members_to_json = jsons.dump(group_members)
        return group_members_to_json

    class Meta:
        model = PatientGroup
        fields = ('id','name', 'description', 'group_messages', 'group_members')


class MessagesSerializer(serializers.ModelSerializer):

    receiver_expert = PatientProfileSerializer(read_only=True)

    class Meta:
        model = Messages
        fields = ['message', 'receiver_expert']
