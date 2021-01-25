from rest_framework import serializers
from login import models
from .models import User,UserDetails
from django.contrib import auth 
from rest_framework.exceptions import AuthenticationFailed
from django.db import IntegrityError
from django_filters import rest_framework as filters
import datetime

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a user profile object"""
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.User
        fields = ['url','id','email','username','password','is_active','is_staff','is_superuser']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    # role = serializers.CharField(source='User.is_superuser',read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens','is_superuser']
        # read_only_fields=['is_superuser',]

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
            'tokens': user.tokens,
            'is_superuser':user.is_superuser,
            
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

class CheckInSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(source='emp_name.email',read_only=True)
    time = serializers.TimeField(format="%H:%M:%S", default=datetime.date.today(),read_only=True)

    class Meta:
        model = models.Attendance
        fields = ['id','checkin','checkout','date','time','email']

class CheckOutSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(source='emp_name.email',read_only=True) 
    time = serializers.TimeField(format="%H:%M:%S", default=datetime.date.today(), read_only=True)
    
    class Meta:
        model= models.Attendance
        fields=['id','checkin','checkout','date','time','email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['username','id', 'email','password','first_name','last_name','address','phone_number','department','position','date_joined','document','photo' ]

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
  

class LeaveSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Leave
        fields = '__all__'

    
class SalaryReportSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='emp.email', read_only=True)
    first_name = serializers.CharField(source='emp.first_name', read_only=True)
    last_name = serializers.CharField(source='emp.last_name', read_only=True)
    year = serializers.SerializerMethodField()
    
    def get_year(self, obj):
        year = obj.received_date.strftime('%Y')
        return year

    class Meta:
        model = models.Salary
        fields = ['id', 'amount','emp','allowance','year','month','received_date','email','first_name','last_name']


class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = UserDetails
        fields = ['username','id', 'email','password','first_name','last_name','address','phone_number','department','date_joined','document','photo' ]

    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     username = attrs.get('username', '')

    #     if not username.isalnum():
    #         raise serializers.ValidationError(
    #             self.default_error_messages)
    #     return attrs

    # def create(self, validated_data):
    #     return UserDetails.objects.create_user(**validated_data)

class EmailVerificationSerializeruserDetail(serializers.Serializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = UserDetails
        fields = ['token']
