from rest_framework import serializers

from authapp.models import CustomUser, PatientProfile


class CustomUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'firstname',
                  'lastname', 'role', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
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


class PatientProfileSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = PatientProfile
        fields = ('id', 'name', 'owner')
