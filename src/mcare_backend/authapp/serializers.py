import jsons

from rest_framework import serializers

from authapp.models import CustomUser

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from patients.models import PatientProfile
from experts.models import ExpertProfile
from experts.serializers import ExpertClassSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializser for custom user model

    Arguments:
        serializers {ModelSerializer} -- creates field that corresponds to the
        custom user model

    Raises:
        serializers.ValidationError: for password mismatch

    Returns:
        serialized object
    """

    tokens = serializers.SerializerMethodField()
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def get_tokens(self, CustomUser):
        """Get token pair for users

        Arguments:
            CustomUser {cls} -- the custom user model

        Returns:
            array -- An array of token
        """

        if self.context['request'].POST:
            refresh = RefreshToken.for_user(self.context['request'].user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
                }
            return data

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'firstname',
                  'lastname', 'role', 'password', 'password2', 'tokens']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        """Over-riding the defaut save on serializers

        Raises:
            serializers.ValidationError: for password mismatch

        Returns:
            user object -- Sets the password and returns the user.
        """

        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            role=self.validated_data['role'],
            firstname=self.validated_data['firstname'],
            lastname=self.validated_data['lastname']
            )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})

        user.set_password(password)
        user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # added username to responses
        # this can be used to the profile page for the user
        # get more personalised content for the user
        data['user_id'] = self.user.id
        return data


class PatientProfileSerializer(serializers.ModelSerializer):
    """Model Serializer foor the Patient Profile Model. Needed to serialize
    patient-profile-specific data

    Args:
        serializers (Model): Serializes the patient profile model
    """

    assigned_experts = serializers.SerializerMethodField()

    def get_assigned_experts(self, PatientProfile):
        my_experts = ExpertProfile.objects.filter(
            assigned_patients__user_id__exact=self.context['request'].user.id
            ).values(
                'user__id',
                'user__username',
                'user__firstname',
                'user__lastname',
                'bio'
            )
        my_experts_to_json = jsons.dump(
            my_experts)  # gets the queryset serlizable
        return my_experts_to_json
    list_of_classes = ExpertClassSerializer(many=True)

    message = serializers.ListSerializer(child=serializers.CharField())
    user = serializers.StringRelatedField()

    class Meta:
        model = PatientProfile
        fields = [
            'id',
            'user',
            'assigned_experts',
            'list_of_classes',
            'message',
            'group_member'
        ]


class ExpertProfileSerializer(serializers.ModelSerializer):
    """An expert profile serializer class

    Arguments:
        serializers {ModelSerializer} -- serializes according to the
        expert profile model
    """

    list_of_classes = serializers.ListSerializer(child=serializers.CharField())

    assigned_patients = PatientProfileSerializer(many=True)

    class Meta:
        model = ExpertProfile
        fields = ['user_id', 'bio', 'list_of_classes', 'assigned_patients']


class PatientUserSerializer(serializers.ModelSerializer):
    """A nested model serializer. Primarily from CustomUser model excluding
    the experts, nesting the PatientProfile Serializer

    Args:
        serializers (nested model): A nested model serializer
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


class ExpertUserSerializer(serializers.ModelSerializer):
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
