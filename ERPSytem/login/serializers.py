from rest_framework import serializers
from login import models
from .models import User


# class HelloSerailizer(serializers.Serializer):
#     name = serializers.CharField(max_length=10)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']





# class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
#     """Serializes a user profile object"""

#     class Meta:
#         model = models.User
#         fields = ['url', 'id', 'email', 'name','password',
#                   'is_active', 'is_staff','is_superuser']

#     def create(self, validated_data):
#         """Create and return a new user"""
#         user = models.User.objects.create_user(
#             email=validated_data['email'],
#             name=validated_data['name'],
#             password=validated_data['password']
#         )

#         return user

# class RegisterSerializer(serializers.ModelSerializer):
#     """Serializes a user profile object"""

#     class Meta:
#         model = models.RegisterUser
#         fields = '__all__'
    

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