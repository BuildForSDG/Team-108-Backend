from rest_framework import serializers
from patients.models import PatientProfile, Messages, PatientGroup, ExpertClass

from authapp.models import CustomUser, ExpertProfile


'''
This RelatedField classes allows the flexibility of the model in the response object.
By default, the pk is displayed in the post or get request. By defining this
class, we can specify how we want the message to be represented in the
reponse
reference: https://stackoverflow.com/questions/55161052/instead-of-primary-key-send-different-field-in-django-rest-framework
'''


# todo what's the related field in seriliazers
# todo so many repetitions. RelatedField Class and their methods,
# todo DRY code needed here
class MessagesRelatedField(serializers.RelatedField):

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return Messages.objects.get(name=data)


class CustomUserRelatedField(serializers.RelatedField):

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return CustomUser.objects.get(name=data)


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

    message = MessagesRelatedField(
        queryset=Messages.objects.all(),
        many=True
    )

    user = CustomUserRelatedField(
        queryset=CustomUser.objects.all(),
    )

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

    class Meta:
        model = PatientProfile
        fields = '__all__'
