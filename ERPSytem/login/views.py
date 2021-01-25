from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from login import serializers
from rest_framework import viewsets
from login import models
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication 
# from login import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions
from django.core.mail import send_mail
from django .conf import settings
from .serializers import RegisterSerializer,EmailVerificationSerializer, UserDetailSerializer,EmailVerificationSerializeruserDetail

from rest_framework import generics, status, views, permissions
from rest_framework import filters as filterss
from .models import User,UserDetails
from rest_framework_simplejwt.tokens import RefreshToken

from .utils import Util , EmailThread
from django.urls import reverse
import jwt
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .overide import IsAssigned
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.throttling import UserRateThrottle,ScopedRateThrottle
from rest_framework.exceptions import Throttled, PermissionDenied
import datetime
from .throttling import CheckInThrottle, CheckOutThrottle

class RegisterView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    serializer_class = RegisterSerializer
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)

   

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        # import pdb;pdb.set_trace()
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.username + \
            ' Use the link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

    
class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()
    # permission_classes = [IsAssigned]


    def get_permissions(self):
    
        if self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
       
    @action(detail=False,methods=['GET'],permission_classes = [IsAssigned,])
    def viewuserdetail(self,request,pk=None):
        # import pdb;pdb.set_trace()
        user=request.user
        serializer=serializers.UserDetailSerializer(user)
        return Response(serializer.data, status=200)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.data , status=status.HTTP_401_UNAUTHORIZED)
    
    def perform_create(self, serializer):

        serializer.save(is_superuser=self.request.user)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = serializers.LogoutSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)   
    


class DeptViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAdminUser,]
    serializer_class = serializers.DeptSerializer
    queryset = models.Department.objects.all()
    # permission_classes = [permissions.IsAdminUser]

class CustomExcpetion(PermissionDenied):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Duplicate Request"
    default_code = "invalid"
 
    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code  

class CheckInViewSet(viewsets.ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.CheckInSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes =  [CheckInThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['emp_name','date']
    
    
    def throttled(self, request,wait):
        raise Throttled(detail={"Messages": "No more check-In allowed.",
                            "AvailableIn": f"{wait} seconds"})

    def perform_create(self, serializer):
        serializer.save(emp_name=self.request.user)

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.CheckOutSerializer
    permission_classes = [permissions.IsAuthenticated ]
    throttle_classes = [CheckOutThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['emp_name','date']

    def throttled(self, request,wait):
        raise Throttled(detail={"Messages": "Time's up. Wait for ",
                                "AvailableIn": f"{wait} seconds"})

    def perform_create(self, serializer):
        CheckedIn = models.Attendance.objects.filter(emp_name=self.request.user.id,date=datetime.date.today(),checkin=True,checkout=False)
        print(CheckedIn)
        print(self.request.user.id)
        if not CheckedIn:
            raise CustomExcpetion(detail={"Error": "Not Checked In.","Check-In": "Before checking out."})
        serializer.save(emp_name=self.request.user)

class LeaveViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.LeaveSerializer
    queryset = models.Leave.objects.all() 
    permission_classes = [permissions.IsAuthenticated ]
   
# class IsOwner(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.user:
#             if request.user.is_superuser:
#                 return True
#             else:
#                 return obj.owner == request.user
#         else:
#             return False

# class IsOwnerOrAdmin(permissions.IsAuthenticated):
#     def has_object_permission(self, request, view, obj):
#         # if request.method in permissions.SAFE_METHODS:
#         #     return True
#         return obj.owner == request.user or request.user.is_superuser

class SalaryReportApiView(viewsets.ModelViewSet):
    """Handlig creating, updating salary field"""
    queryset = models.Salary.objects.all()
    serializer_class = serializers.SalaryReportSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filterss.SearchFilter]
    filterset_fields = ['amount','month','emp']
    search_fields = ['^emp__email','^month','^emp__first_name','^emp__last_name','year']
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset=models.Salary.objects.all().order_by('-received_date')
            return queryset

        queryset = self.queryset
        query_set =  queryset.filter(emp=self.request.user).order_by('-received_date')
        # print(query_set)
        return query_set

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated,]
        # elif self.action =='list':
        #     permission_classes=[IsAdminUser,]
        # elif self.action=='retrieve': 
        #     permission_classes = [IsOwnerOrAdmin,]
        else:
            permission_classes=[IsAdminUser]
        return [permission() for permission in permission_classes]
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         permission_classes =[IsOwnerOrAdmin]
    #     elif self.action == 'list':
    #         self.permission_classes = [permissions.IsAdminUser ]
    #     elif self.action == 'retrieve':
    #         self.permission_classes = [IsOwnerOrAdmin]
    #     else:
    #         self.permission_classes=[IsAdminUser]
    #     return super(self.__class__, self).get_permissions()

    @action(detail=False,methods=['GET'], permission_classes=[IsAuthenticated])
    def salary_report(self,request):
        user= request.user 
        salary=models.Salary.objects.filter(emp=user)
        serializer=serializers.SalaryReportSerializer(salary,many=True)   
        return Response(serializer.data, status=200)

class UserDetailView(generics.GenericAPIView):

    serializer_class = serializers.UserDetailSerializer
    # queryset = models.UserDetails.objects.all()
    queryset = UserDetails.objects.all()

    serializer_class = UserDetailSerializer


    @action(detail=False,methods=['GET'],permission_classes = [IsAssigned,])
    def viewdetail(self,request,pk=None):
        user=request.user
        serializer=serializers.UserDetailSerializer(user)
        return Response(serializer.data, status=200)
     
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = UserDetails.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        # import pdb;pdb.set_trace()
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify1')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.username + \
            ' Use the link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmailUserDetail(views.APIView):
    serializer_class = EmailVerificationSerializeruserDetail

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = UserDetails.objects.get(id=payload['user_id'])
            
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserDetailSerializer
    queryset = models.UserDetails.objects.all()
    # permission_classes = [IsAssigned]


    def get_permissions(self):
    
        if self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False,methods=['GET'],permission_classes = [IsAssigned,])
    def userdetail(self,request,pk=None):
        user=request.user
        serializer=serializers.UserDetailSerializer(user)
        return Response(serializer.data, status=200)