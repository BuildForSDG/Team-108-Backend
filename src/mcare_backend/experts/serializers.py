import jsons
from rest_framework import serializers

from patients.models import PatientProfile, Messages
from authapp.models import CustomUser
from experts.models import ExpertProfile, ExpertClass, ClassModules


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


class ClassModulesRelatedField(serializers.RelatedField):

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return ClassModules.objects.get(name=data)


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


class PatientProfileRelatedField(serializers.RelatedField):

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return PatientProfile.objects.get(name=data)


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


class ExpertProfileSerializer(serializers.ModelSerializer):

    message = MessagesRelatedField(
        queryset=Messages.objects.all(),
        many=True
    )

    user = CustomUserRelatedField(
        queryset=CustomUser.objects.all(),
    )

    assigned_patients = PatientProfileRelatedField(
        queryset=PatientProfile.objects.all(),
        many=True
    )

    list_of_classes = ExpertClassRelatedField(
        queryset=ExpertClass.objects.all(),
        many=True
    )

    class Meta:
        model = ExpertProfile
        fields = '__all__'


class ExpertClassSerializer (serializers.ModelSerializer):

    members = ExpertClassRelatedField(
        queryset=ExpertClass.objects.all(),
        many=True
    )

    class_modules = ClassModulesRelatedField(
        queryset=ClassModules.objects.all(),
        many=True
    )

    message = serializers.SerializerMethodField()

    def get_message(self, ExpertClass):
        mess = Messages.objects.filter(
            receiver_class_id=ExpertClass.id).values(
                'author_id__username', 'message')
        mess = jsons.dump(mess)  # gets the queryset serlizable
        return mess

    class Meta:
        model = ExpertClass
        fields = '__all__'
