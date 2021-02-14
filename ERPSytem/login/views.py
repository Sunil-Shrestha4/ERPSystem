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
from .serializers import RegisterSerializer,EmailVerificationSerializer, UserDetailSerializer,EmailVerificationSerializeruserDetail,AdminLeaveSerializer,UserLeaveSerializer,ManagerLeaveSerializer,LeaveTypeSerializer,MyLeaveSerializer

from rest_framework import generics, status, views, permissions
from .models import User,UserDetails,Attendance,Leave,MyLeave
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
# from django_filters import rest_framework as filters
from rest_framework.throttling import UserRateThrottle ,ScopedRateThrottle
from rest_framework.exceptions import Throttled ,PermissionDenied
from rest_framework import throttling
import datetime
from rest_framework import filters


class CheckinRateThrottle(throttling.UserRateThrottle):
    scope = 'checkin'
    rate = '1/min'

class CheckoutRateThrottle(throttling.UserRateThrottle):
    scope = 'checkout'
    rate = '3/min'



class RegisterView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]
    # import pdb;
    # pdb.set_trace()

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
                    'Here are the details you may need while login in our system \n'+ \
                    'User Name:'+user.username  +\
                    "Password:"+ user.password  +\
                    ' Use the link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class RUDRegisterView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    serializer_class = RegisterSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    
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
    queryset = models.User.objects.all().select_related('department')
    filter_backends=[DjangoFilterBackend,filterss.SearchFilter]
    permission_classes=[ permissions.IsAuthenticatedOrReadOnly]
    filterset_fields=['username']
    search_fields=['^username','^email','^first_name','^last_name','^department','^address']

    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         queryset=models.User.objects.all().order_by('-date_joined')
    #         return queryset


    # def get_permissions(self):
    #     if self.request.method=='GET':
    #         permission_classes=[IsAuthenticated,]
    #     else:
    #         permission_classes=[IsAdminUser]
    #     return [permission() for permission in permission_classes]
        

        # queryset = self.queryset
        # query_set=queryset.filter(emp=self.request.user).order_by('-date_joined')
        # return query_set









    # permission_classes = [IsAssigned]


    # def get_permissions(self):
    
    #     if self.request.method == 'GET':
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]

    # def get_permissions(self):
        
    #     if self.request.method == 'POST':
    #         self.permission_classes = [permissions.IsAdminUser ]
    #     elif self.request.method == 'PUT':
    #         self.permission_classes = [permissions.IsAdminUser ]
    #     elif self.request.method == 'DELETE':
    #         self.permission_classes = [permissions.IsAdminUser ]
    #     elif self.request.method == 'PATCH':
    #         self.permission_classes = [permissions.IsAdminUser ]
    #     elif self.request.method == 'HEAD':
    #         self.permission_classes = [permissions.IsAdminUser ]


    #     else:
    #         self.permission_classes = [IsAuthenticated, ]
        

    #     return super(UserProfileViewSet, self).get_permissions()



    

    

    # def get_permissions(self): 
    
    #     if self.request.method == 'GET':
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]
  
    @action(detail=False,methods=['GET'])
    def viewuserdetail(self,request,pk=None):
        # import pdb;pdb.set_trace()
        user=request.user
        serializer=serializers.UserProfileSerializer(user)
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
    # permission_classes = [permissions.IsAdminUser,]
    serializer_class = serializers.DeptSerializer
    queryset = models.Department.objects.all()
    # permission_classes = [permissions.IsAdminUser]

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AttendanceSerializer
    queryset = models.Attendance.objects.all()
    permission_classes = [permissions.IsAuthenticated ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['emp_name']
    
    filter_backends = [DjangoFilterBackend , filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['emp_name','date']
    search_fields=['^emp_name__first_name']
    ordering_fields={'time','date'}
    # import pdb; pdb.set_trace()
    http_method_names = [u'get', u'delete', u'head', u'options', u'trace']

    def filter_queryset(self, queryset):
       
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
            
            # if not queryset:
            #     raise CustomExcpetion(detail={"ERROR": "Not found","NOTE": "Search by other valid names"})
                
            # import pdb; pdb.set_trace()
        return queryset
            
    @action(detail=False, methods=['GET'])
    def view(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(emp_name=request.user )
        serializer = serializers.AttendanceSerializer(queryset, many=True) 
        return Response(serializer.data)
        
    def perform_create(self, serializer):
        serializer.save(emp_name=self.request.user)

    @action(detail=False, methods=['GET'])
    def delete_by_empname(self, request):
        # import pdb; pdb.set_trace()
        queryset = self.filter_queryset(self.get_queryset()).filter(emp_name_id=request.user.id)
        
        
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CheckInViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CheckInSerializer
    queryset=models.Attendance.objects.all()
    throttle_scope='checkin'
    throttle_classes=[CheckinRateThrottle]
    def throttled(self, request, wait):
        raise Throttled(detail={
              "message":"kripaya aja lai chekin garna payinexaina tesaile checkout garnu hola",
              "availableIn":f"{wait} seconds",
        })
    
    def perform_create(self, serializer):
        serializer.save(emp_name=self.request.user)

class CustomExcpetion(PermissionDenied):
   status_code = status.HTTP_400_BAD_REQUEST
   default_detail = "Duplicate Request"
   default_code = "invalid"
 
   def __init__(self, detail, status_code=None):
       self.detail = detail
       if status_code is not None:
           self.status_code = status_code


class CheckOutViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CheckOutSerializer
    queryset=models.Attendance.objects.all()
    throttle_scope='checkout'
    throttle_classes=[CheckoutRateThrottle]
    def throttled(self, request, wait):
        raise Throttled(detail={
              "message":"aja lai chekout garna payinexaina ",
              "availableIn":f"{wait} seconds",
        })
    def perform_create(self, serializer):
       notCheckedIn = models.Attendance.objects.filter(emp_name=self.request.user,date=datetime.date.today(),choices={'checkin':True})
       print(notCheckedIn)
       if not notCheckedIn:
           raise CustomExcpetion(detail={"Error": "Not Checked In.","Check-In": "Before checking out."})
            # return Response(status=status.HTTP_400_BAD_REQUEST)
       serializer.save(emp_name=self.request.user)
    
    # def perform_create(self, serializer):
        
    #     serializer.save(emp_name=self.request.user)

        # serializer = serializers.MyLeaveSerializer(queryset, many=True)
        # # import pdb;pdb.set_trace()
        # return Response(serializer.data)
                      
# class SalaryReportApiView(viewsets.ModelViewSet):
#     """Handli ccreating, updating salary field"""
#     queryset = models.Salary.objects.all()
#     serializer_class=serializers.SalaryReportSerializer
#     permission_classes=[IsAdminUser]
#     filter_backends=[DjangoFilterBackend,filterss.SearchFilter]
#     filterset_fields=['amount','month','emp']
#     search_fields=['^emp__email','^month','^emp__first_name','^emp__last_name','^year']
    

    
#     def throttled(self, request,wait):
#         raise Throttled(detail={"Messages": "No more check-In allowed.",
#                             "AvailableIn": f"{wait} seconds"})

#     def perform_create(self, serializer):
#         serializer.save(emp_name=self.request.user)

class SalaryReportApiView(viewsets.ModelViewSet):
    """Handlig creating, updating salary field"""
    queryset = models.Salary.objects.all()
    serializer_class = serializers.SalaryReportSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['amount','month','emp']
    search_fields = ['^emp__email','^month','^emp__first_name','^emp__last_name','year']
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset=models.Salary.objects.all().order_by('id')
            return queryset

        queryset = self.queryset
        query_set =  queryset.filter(emp=self.request.user).order_by('id')
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
            permission_classes=[IsAdminUser,]
        return [permission() for permission in permission_classes]

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



    
