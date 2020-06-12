from rest_framework import serializers

from authapp.models import CustomUser

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
