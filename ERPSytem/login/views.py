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
from .serializers import RegisterSerializer,EmailVerificationSerializer, UserDetailSerializer,EmailVerificationSerializeruserDetail,AdminLeaveSerializer,UserLeaveSerializer,ManagerLeaveSerializer,LeaveTypeSerializer,MyRemainingLeaveSerializer,ChangePasswordSerializer,HolidaySerializer,DailyUpdateSerializer

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
from .overide import IsAssigned,IsOwnerOrAdmin,IsAbc,IsSuperUser,IsOwner
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
# from django_filters import rest_framework as filters
from rest_framework.throttling import UserRateThrottle ,ScopedRateThrottle
from rest_framework.exceptions import Throttled ,PermissionDenied
from rest_framework import throttling
import datetime
from rest_framework import filters
from rest_framework import filters as filterss

from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
# from .renderers import UserRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from datetime import date
from django.db.models import Q




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


class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset=models.LeaveType.objects.all()
    serializer_class=serializers.LeaveTypeSerializer
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
    
    


class LeaveViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.AdminLeaveSerializer
    queryset = models.Leave.objects.all() 
    permission_classes = [permissions.IsAuthenticated ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee']

    queryset=Leave.objects.all()


    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminLeaveSerializer
        elif self.request.user.is_manager:
            return ManagerLeaveSerializer
        else:
            return UserLeaveSerializer

    def perform_create(self,serializer):
        
        # import pdb; pdb.set_trace()
        ids=serializer.validated_data['types_of_leave'].id
        
        total_days =   models.LeaveType.objects.get(id=ids).days
        
        obj_user=models.Leave.objects.filter(employee=self.request.user.id)
        obj=obj_user.filter(types_of_leave=serializer.validated_data['types_of_leave'])
        # import pdb; pdb.set_trace()


        # if obj_user.exists():
            
        #     remaining_day=serializer.validated_data['remainingday']-serializer.validated_data['number_of_days']

            # return total_days
        if obj_user.exists() and obj.exists():
            remaining=models.Leave.objects.filter(employee=self.request.user.id) .filter(types_of_leave=serializer.validated_data['types_of_leave']).last().__dict__
            remaining_day=remaining['remainingday']
        # # remainingday=remaining['remainingday']
            remainingday=remaining_day
            # remaining_day=remainingday-serializer.validated_data['number_of_days']
        # import pdb; pdb.set_trace()

        else:
            remainingday =total_days
        
            # remaining_day=total_days-serializer.validated_data['number_of_days']
            # return remainingday
        # import pdb; pdb.set_trace()
        # remainingday=total_days-user.number_of_days
    
        user=serializer.save(employee=self.request.user,remainingday=remainingday)
        # for e in models.Leave.objects.filter( id=27).values():
        #     remainingday=e['remainingday']
        # # remaining=models.Leave.objects.filter(employee=self.request.user.id).order_by('-id').last().__dict__
        # # remainingday=remaining['remainingday']
        # # import pdb; pdb.set_trace()
        # if remainingday==total_days:
        #     serializer.save(remainingday=total_days)

            
        # else:

        #     day = remainingday-user.number_of_days
        #     serializer.save(remainingday=day)
            

          
        serializer.data        
        e_subject = "Leave Verification"
        e_msg = "Here are the details about the leave\n"+"User Name:"+user.employee.username+"\n"+"Ëmail:"+user.employee.email+"\n"+"start date:"+str(user.start)+"\n"+"End date:"+str(user.end)+"\n"+"Number of days:"+str(user.number_of_days)+"\n"+"Reason:"+user.reason+"Verify:"+"http://127.0.0.1:8000/api/leave/"+str(user.id)
        e_mail = settings.EMAIL_HOST_USER
        email=User.objects.filter(is_manager=True).values_list('email',flat=True)
        Email=list(email)
        # import pdb; pdb.set_trace()

        send_mail(
            e_subject,
            e_msg,
            e_mail,
            Email,
            fail_silently=False
        )


    def perform_update(self, serializer):
        
        user=serializer.save()
        obj1=self.get_object()
        ids=serializer.validated_data['types_of_leave'].id
        total_days =   models.LeaveType.objects.get(id=ids).days

        # obj_user=models.Leave.objects.filter(employee=self.request.user.id)
        # obj=obj_user.filter(types_of_leave=serializer.validated_data['types_of_leave'])
        # import pdb;pdb.set_trace()

        # if obj_user.exists():
        #     remainingday=remainingday-user.number_of_days

        if obj1.is_verified==True:

            # import pdb;pdb.set_trace()
            # numner_of_days=self.validated_data.get('number_of_days')
            # import pdb; pdb.set_trace()
            # if obj_user.exists() and obj.exists():
                # remainingday=remainingday-user.number_of_days
                # remainingday=remaining_day

                # remaining=models.Leave.objects.filter(employee=self.request.user.id).order_by('-id').first().__dict__
                # remainingday=remaining['remainingday']
            # remaining = serializer.data
            # remaining.is_valid(raise_excpetions=True)
            # remainingday = remaining.validated_data.get('remainingday')
            # abc=serializer.data
            # abc.is_valid()
            # remaininginstance=abc.save()
            # number=abc.number_of_days

        
            # serializer.validated_data
            # remainingday=serializer.validated_data['number_of_days']

            remainingday=user.remainingday-user.number_of_days
            serializer.save(remainingday=remainingday)
            
            # ser=serializer.data
            # # ser. is_valid(raise_exceptions=True)
            # data=ser.validated_data
            # remainingday=obj1.remainingday- data['number_of_days']
            # serializer.save(remainingday=remainingday)
            # # import pdb;pdb.set_trace()


        # else:
            
        #         remaining_day =total_days
        
            #     # remaining_day=total_days-serializer.validated_data['number_of_days']
            #     remaining_day=remainingday
            
        # else:
        #     if obj.exists():
        #         remaining=models.Leave.objects.filter(employee=self.request.user.id).order_by('-id').first().__dict__
        #         remainingday=remaining['remainingday']
        #     # # remainingday=remaining['remainingday']
        #         remaining_days=remainingday
        #         # remaining_day=remainingday-serializer.validated_data['number_of_days']
            # import pdb; pdb.set_trace()

        else:
            remainingday =user.remainingday
            serializer.save(remainingday=remainingday)
        
        # import pdb;pdb.set_trace()


        


            # day = total_days-user.number_of_days
            
        # serializer.save(remainingday=remaining_days)
        # user=serializer.save()
            # serializer.save(total_days=day)
        
        # else:
        #     serializer.save(remainingday=total_days)

        if self.request.user.is_manager:
            # permission_classes = [IsAbc ]

            if user.is_notapproved==True and user.is_approved==False :
                e_subject = "Leave Rejected"
                e_msg = "Sorry your leave hasnot been approved by Manager. Contact for further details"
                e_mail = settings.EMAIL_HOST_USER
                Email=user.employee.email


                send_mail(
                    e_subject,
                    e_msg,
                    e_mail,
                    [Email]

                )
            elif user.is_approved==True and user.is_notapproved==False:
                
                e_subject = "Leave Approval"
                e_msg = "Here are the details about the leave\n"+"User Name:"+user.employee.username+"\n"+"Ëmail:"+user.employee.email+"\n"+"start date:"+str(user.start)+"\n"+"End date:"+str(user.end)+"\n"+"Number of days:"+str(user.number_of_days)+"\n"+"Reason:"+user.reason+"Verify:"+"http://127.0.0.1:8000/api/leave/"+str(user.id)
                e_mail = settings.EMAIL_HOST_USER
                email=User.objects.filter(is_superuser=True).values_list('email',flat=True)
                Email=list(email)
                send_mail(
                    e_subject,
                    e_msg,
                    e_mail,
                    Email,
                    fail_silently=False

                )

                
        elif self.request.user.is_superuser:
            permission_classes = [permissions.IsAdminUser ]

            if user.is_notverified==True and user.is_verified==False:
                e_subject = " Leave Rejected"
                e_msg = "Your leave is approved but not verified. Please contact for further details"
                e_mail = settings.EMAIL_HOST_USER
                Email=user.employee.email

                send_mail(
                    e_subject,
                    e_msg,
                    e_mail,
                    [Email]

                )
            
            elif user.is_notverified==False and user.is_verified==True:



            # import pdb;pdb.set_trace()
                e_subject = " Leave Approved"
                e_msg = "Your leave is approved"
                e_mail = settings.EMAIL_HOST_USER
                Email=user.employee.email

                send_mail(
                    e_subject,
                    e_msg,
                    e_mail,
                    [Email]

                )
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def MyLeaveHistory(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(employee=request.user)
        serializer = serializers.UserLeaveSerializer(queryset, many=True) 
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def MyRemainingLeave(self,request,**kwargs):

        
        
       
    
        queryset = self.filter_queryset(self.get_queryset()).filter(employee=request.user)
        # obj1=self.get_object()
       

        # import pdb;pdb.set_trace()
        leavetype1=models.Leave.objects.filter(Q(types_of_leave=1) | Q(types_of_leave=2) | Q(types_of_leave=3)).last()
        serializer =serializers.MyRemainingLeaveSerializer(leavetype1,many=False)
        # queryset=.filter(types_of_leave=1).last()
      
        # queryset=queryset.filter(types_of_leave=value).latest(id)
        
        return Response(serializer.data)



class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = serializers.ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HolidayViewSet(viewsets.ModelViewSet):
    queryset=models.Holiday.objects.filter(Q(date_of_event__gte=date.today()) | Q(date_of_event=date.today())).order_by('date_of_event')
    serializer_class=serializers.HolidaySerializer

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

class DailyUpdateViewSet(viewsets.ModelViewSet):
    queryset=models.DailyUpdate.objects.all()
    serializer_class=serializers.DailyUpdateSerializer


    def perform_create(self,serializer):
        # user=self.request.user

    

        # queryset=models.DailyUpdate.objects.filter(employee=user)
        # serializer=serializers.DailyUpdateSerializer(queryset,many=False)
        # 


        # def get_queryset(self):
        #     user=self.request.user
        #     return models.DailyUpdate.filter(name=user)
        serializer.save(employee=self.request.user)

    # #     def get_queryset(self):
    # #         user=self.request.user
    # #         return models.DailyUpdate.filter(employee=user)




    
    # # def get_permissions(self):
    # #     if self.action == 'list':
    # #         self.permission_classes = [IsSuperUser, ]
    # #     elif self.action == 'get':
    #         self.permission_classes = [IsOwner]
    #     return super(self.__class__, self).get_permissions()















        # if self.action == 'GET':
        #     permission_classes = [IsAssigned]
        # # elif self.action =='list':
        # #     permission_classes=[IsAdminUser,] 	    
        # # elif self.action=='retrieve': 
        # #     permission_classes = [IsOwnerOrAdmin,]
        # else:
        #     permission_classes=[IsAdminUser,]
        # return [permission() for permission in permission_classes]

    @action(detail=False, methods=['GET'])
    def MyDailyUpdate(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(employee=request.user)
        serializer = serializers.DailyUpdateSerializer(queryset, many=True) 
        return Response(serializer.data)




    


    

    
