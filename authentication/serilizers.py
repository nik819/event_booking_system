from rest_framework import serializers
from authentication.models import User

class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'confirmPassword', 'dateOfBirth', 'username']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Use `create_user` to hash password properly
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            confirmPassword=validated_data['confirmPassword'],
        )
        user.dateOfBirth = validated_data.get('dateOfBirth')
        user.save()
        return user
