from rest_framework import serializers
from login import models
from .models import User,UserDetails, Leave,LeaveType,MyLeave,Holiday
from django.contrib import auth 
from rest_framework.exceptions import AuthenticationFailed
from django.db import IntegrityError
from django_filters import rest_framework as filters
import datetime
from datetime import date
# from django.contrib.auth.tokens import PasswordRestTokenGenerator
# from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodDecodeError
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode



class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.User
        fields = ['id','email','username','password','is_active','is_staff','is_superuser','is_verified','is_manager','first_name','last_name','address','phone_number','department','date_joined','document','photo']
        read_only_fields=['is_verified',]

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
        fields = ['email', 'password', 'username', 'tokens','is_superuser','is_manager']
        read_only_fields=['is_manager',]

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
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens,
            'is_superuser':user.is_superuser,
            'is_manager':user.is_manager,
            
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
    
    # def choices_by_order(self,obj):
class AttendanceSerializer(serializers.ModelSerializer):
    name=serializers.CharField(source='emp_name.first_name',read_only=True)    
    
    class Meta:
        model= models.Attendance
        fields=['id','date','time','name','choices','emp_name']

class CheckInSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='emp_name.first_name',read_only=True)
    checkin= serializers.BooleanField(source='choices.checkin',default=False)
    checkout= serializers.BooleanField(source='choices.checkout',default=False,read_only=True)

    class Meta:
        model= models.Attendance
        fields=['id','date','time','name','checkin','checkout']

class CheckOutSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='emp_name.first_name',read_only=True)
    checkout= serializers.BooleanField(source='choices.checkout')
    checkin= serializers.BooleanField(source='choices.checkout',read_only=True)

    class Meta:
        model= models.Attendance
        fields=['id','date','time','name','checkout','checkin']

class RegisterSerializer(serializers.ModelSerializer):
    department_name=serializers.CharField(source='department.dept_name',read_only=True)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = models.User
        fields = ['username','id','is_superuser','is_verified','is_manager','is_staff', 'email','password','first_name','last_name','address','phone_number','department','date_joined','document','photo','department_name' ]

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


# class ResetPasswordEmailRequestSerializer(serializers.Serializer):
#     email=serializers.EmailField(min_length=2)

#     redirect_url = serializers.CharField(max_length=500,required=False)

#     class Meta:
#         fields=['email']


# class SetNewPasswordSerializer(serializers.Serializer):
#     password = serializers.CharField(
#         min_length=6, max_length=68, write_only=True)
#     token = serializers.CharField(
#         min_length=1, write_only=True)
#     uidb64 = serializers.CharField(
#         min_length=1, write_only=True)

#     class Meta:
#         fields = ['password', 'token', 'uidb64']

#     def validate(self, attrs):
#         try:
#             password = attrs.get('password')
#             token = attrs.get('token')
#             uidb64 = attrs.get('uidb64')

#             id = force_str(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(id=id)
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 raise AuthenticationFailed('The reset link is invalid', 401)

#             user.set_password(password)
#             user.save()

#             return (user)
#         except Exception as e:
#             raise AuthenticationFailed('The reset link is invalid', 401)
#         return super().validate(attrs)





  

class LeaveTypeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=LeaveType
        fields =['id','leavetype','days']

class MyRemainingLeaveSerializer(serializers.ModelSerializer):
    leave_Category=serializers.CharField(source='types_of_leave.leavetype',read_only=True)
    remainingday=serializers.IntegerField(read_only=True)
    # leavetype=serializers.CharField(source='leave.leavetype')
    # total_days=serializers.CharField(source='leave.days')
    # # numberof_requestday=serializers.CharField(source='days.number_of_days')
    # remaining_days=serializers.SerializerMethodField()
    # import pdb; pdb.set_trace()

    # def get_remaining_days(self,obj):
        # remaining_days=Ltotal_days-numberof_requestday
        # return remaining_days

    class Meta:
        model=Leave

        fields=['id','leave_Category','types_of_leave','remainingday']

    

class AdminLeaveSerializer(serializers.ModelSerializer):
    leave_Category=serializers.CharField(source='types_of_leave.leavetype',read_only=True)
    name=serializers.CharField(source='employee.first_name',read_only=True)
    email=serializers.CharField(source='employee.email',read_only=True)
    # number_of_days = serializers.IntegerField()
    # start= serializers.DateField()
    # number_of_days = serializers.SerializerMethodField()
    # # import pdb; pdb.set_trace()

    # def get_number_of_days(self, obj):
    #     number_of_days = (obj.end - obj.start).days
    #     # print(obj.start) 
    #     return number_of_days
    number_of_days = serializers.IntegerField()
    remainingday=serializers.IntegerField(read_only=True)

    # def get_number_of_days(self, obj):
    #     number_of_days = (obj.end - obj.start).days
    #     # print(obj.start) 
    #     return number_of_days



    class Meta:
        model=Leave
        fields=['id','is_approved','is_notapproved','is_verified','is_notverified','start','end','types_of_leave','leave_Category','number_of_days','reason','name','email','remainingday']
        # write_only_fields=('types_of_leave')
       
class ManagerLeaveSerializer(serializers.ModelSerializer):
    types_of_leaves=serializers.CharField(source='types_of_leave.leavetype',read_only=True)
    name=serializers.CharField(source='employee.first_name',read_only=True)
    email=serializers.CharField(source='employee.email',read_only=True)

    number_of_days = serializers.IntegerField()
    remainingday=serializers.IntegerField(read_only=True)

    # def get_number_of_days(self, obj):
    #     number_of_days = (obj.end - obj.start).days
    #     # print(obj.start) 
    #     return number_of_days

    class Meta:
        model=Leave
        fields=['id','is_approved','is_verified','is_notverified','is_notapproved','start','end','types_of_leave','types_of_leaves','number_of_days','reason','name','email','remainingday']

        
        read_only_fields=['is_verified','is_notverified']


class UserLeaveSerializer(serializers.ModelSerializer):
    types_of_leaves=serializers.CharField(source='types_of_leave.leavetype',read_only=True)
    name=serializers.CharField(source='employee.first_name',read_only=True)
    email=serializers.CharField(source='employee.email',read_only=True)
    remainingday=serializers.IntegerField(read_only=True)
    # totaldays=serializers.IntegerField(source='types_of_leave.days',read_only=True)

    # number_of_days = serializers.IntegerField()
    number_of_days = serializers.IntegerField()

    # def get_number_of_days(self, obj):
    #     number_of_days = (obj.end - obj.start).days
    #     # print(obj.start) 
    #     return number_of_days

    # # # remainingdays= serializers.SerializerMethodField()

    # def get_number_of_days(self, obj):

    #     number_of_days = (obj.end - obj.start).days


    #     # print(obj.start) 
    #     return number_of_days

    # def get_remaining_days(self,obj):
    #     remaining_days=(obj.totaldays-obj.number_of_days)
    #     print(remaining_days)
    #     return remaining_days
    
    class Meta:
        model=Leave
        fields=['id','is_approved','is_verified','start','end','employee','types_of_leave','types_of_leaves','number_of_days','reason','name','email','remainingday']

        
        read_only_fields=['is_approved','is_verified',]
    


# class MyLeaveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=MyLeave
#         fields=[__all__]

    
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
        fields = ['url','username','id', 'email','password','first_name','last_name','address','phone_number','department','date_joined','document','photo' ]

class EmailVerificationSerializeruserDetail(serializers.Serializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = UserDetails
        fields = ['token']





class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class HolidaySerializer(serializers.ModelSerializer):
    
    remainingday=serializers.SerializerMethodField()

    def get_remainingday(self,obj):
        remainingday=(obj.date_of_event-date.today()).days
        return remainingday
    


    class Meta:
        model = models.Holiday
        fields = ['id','event','date_of_event','remainingday']


