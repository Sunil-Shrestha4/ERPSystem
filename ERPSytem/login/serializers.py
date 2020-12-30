from rest_framework import serializers
from login import models
from .models import User
from django.contrib import auth 
from rest_framework.exceptions import AuthenticationFailed



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
    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     if User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError(
    #             {'email': ('Email is already in use')})
    #     return super().validate(attrs)

    # def create(self, validated_data):
    #     user = super().create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user


# class LoginSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.User
#         fields = ['email','password',]

# # # class UserSerializer(serializers.ModelSerializer):
# # #     class Meta:
# # #         model = User
# # #         fields = ('id', 'username', 'email')

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        # if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
        #     raise AuthenticationFailed(
        #         detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }

        return super().validate(attrs)



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')


class DeptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= models.Department
        fields=('url','dept_name')

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Attendance
        fields='__all__'

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        max_length=70,
        min_length= 6,
        write_only=True,
        required=True,
        style = {'input_type': 'password','placeholder':'password'},
    )

    class Meta:
        model = models.User
        fields = ( 'username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}
    def validate(self, attrs):
        email = attrs.get('email', '')
        username =attrs.get('username','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return attrs

    def create(self, validated_data):
        # user = super().create_user(**validated_data)
        # user.set_password(validated_data['password'])
        # user.save()
        return User.objects.create_user(**validated_data)
    # def create(self, validated_data):
    #     user = models.User.objects.create_user(validated_data['name'], validated_data['email'], validated_data['password'])

    #     return user
    

class LeaveSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Leave
        fields = '__all__'



    
class SalaryReportSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Salary
        fields = ('employee_name','amount','department',)
        extra_kwargs={'amount':{'write_only':True}}
        