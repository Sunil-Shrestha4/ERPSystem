from rest_framework import serializers
from login import models



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
class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Department
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Attendance
        fields='__all__'
    
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