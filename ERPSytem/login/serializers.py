from rest_framework import serializers
from login import models

# class HelloSerailizer(serializers.Serializer):
#     name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.User
        fields = '__all__'

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class RegisterSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.RegisterUser
        fields = '__all__'
    

class LeaveSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Leave
        fields = '__all__'
    


# ('id', 'email', 'name', 'password')
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'style': {'input_type': 'password'}
#             }
#         }