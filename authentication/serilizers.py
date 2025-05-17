from rest_framework import serializers
from authentication.models import User

class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'dateOfBirth', 'username', 'mobileNo', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            dateOfBirth=validated_data['dateOfBirth'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobileNo=validated_data['mobileNo'],
        )
        user.save()
        return user
