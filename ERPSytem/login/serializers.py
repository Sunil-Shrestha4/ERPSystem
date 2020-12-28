from rest_framework import serializers
from login import models
from .models import User



class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.User
        fields = ['url','id','email','name','password','is_active','is_staff','is_superuser']

    # def create(self, validated_data):
    #     """Create and return a new user"""
    #     user = models.User.objects.create_user(
    #         email=validated_data['email'],
    #         name=validated_data['name'],
    #         password=validated_data['password']
    #     )
    #     return user
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.User
#         fields = ['email','password',]


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Department
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Attendance
        fields='__all__'
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
    
class SalaryReportSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Salary
        fields = '__all__'



# ('id', 'email', 'name', 'password')
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'style': {'input_type': 'password'}
#             }
#         }