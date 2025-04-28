from rest_framework import serializers
from authentication.models import User

class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'dateOfBirth', 'mobileNumber', 'first_name', 'last_name', 'username']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            dateOfBirth=validated_data['dateOfBirth'],
            mobileNumber=validated_data['mobileNumber'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
