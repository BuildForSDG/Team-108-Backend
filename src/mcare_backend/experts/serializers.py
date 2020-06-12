import jsons
from rest_framework import serializers

from patients.models import PatientProfile, Messages
from authapp.models import CustomUser
from experts.models import ExpertProfile, ExpertClass, ClassModules


class MessagesRelatedField(serializers.RelatedField):
    """A serliazer class of type related field,
    overides how the output messages in the
    serializers

    Arguments:
        serializers {RelatedField} --
        for defining how the output messages
    """

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
    """A serliazer class of type related field,
    overides how the output class modules in the
    serializers

    Arguments:
        serializers {RelatedField} --
        for defining how the output class modules
    """

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return ClassModules.objects.get(name=data)


class PatientProfileRelatedField(serializers.RelatedField):
    """A serliazer class of type related field,
    overides how the output patient profile in the
    serializers

    Arguments:
        serializers {RelatedField} --
        for defining how the output patient profile
    """

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
    """A serliazer class of type related field,
    overides how the output expert class in the
    serializers

    Arguments:
        serializers {RelatedField} --
        for defining how the output expert class
    """

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
    """An expert profile serializer class

    Arguments:
        serializers {ModelSerializer} -- serializes according to the
        expert profile model
    """

    list_of_classes = serializers.ListSerializer(child=serializers.CharField())

    assigned_patients = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = ExpertProfile
        fields = ['bio', 'list_of_classes', 'assigned_patients']


class CustomUserSerializer(serializers.ModelSerializer):
    """A nexted custom user serializer class. Expertprofile
    serializer is nested in it

    Arguments:
        serializers {ModelSerializer} -- serializes according to the
        custom user model
    """

    expert_profile = ExpertProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'firstname',
            'lastname',
            'email',
            'expert_profile'
            ]


class ExpertClassSerializer (serializers.ModelSerializer):
    """An expert class serializer class

    Arguments:
        serializers {ModelSerializer} -- serializes according to the
        expert class model
    """

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
            receiver_class_id=ExpertClass.id
            ).values(
                'author_id__username', 'message'
                )
        mess = jsons.dump(mess)  # gets the queryset serlizable
        return mess

    class Meta:
        model = ExpertClass
        fields = '__all__'
