import jsons
from rest_framework import serializers

from patients.models import PatientProfile, Messages
from experts.models import ExpertClass, ClassModules

# from authapp.serializers import PatientProfileSerializer


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

    class_modules = serializers.SerializerMethodField()

    def get_class_modules(self, ExpertClass):
        mess = ClassModules.objects.filter(
            expertclass=ExpertClass.id
            ).values(
                'id',
                'title'
            )
        mess = jsons.dump(mess)  # gets the queryset serlizable
        return mess

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
