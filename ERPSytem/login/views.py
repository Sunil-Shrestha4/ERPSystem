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

from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .overide import IsAssigned,IsAbc
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.core.mail import EmailMessage
from django.core.mail import send_mass_mail
from rest_framework import filters as filterss
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView



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


    
    
# class UserProfileViewSet(viewsets.ViewSet):
#     serializer_class = serializers.UserProfileSerializer
#     permission_classes = [IsAuthenticated]
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = models.User.objects.all()
#         serializer = serializers.UserProfileSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = models.User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = serializers.UserProfileSerializer(user)
#         return Response(serializer.data)
    
#     def get_permissions(self):
#         if self.action == 'list':
#             permission_classes = [permissions.IsAuthenticated ]
        
#         # elif self.action == 'retrieve':
#         #     self.permission_classes = [permissions.IsAuthenticated]
#         else:
#             permission_classes =[permissions.IsAdminUser]
#         return [permission() for permission in permission_classes]
    


    # Your logic should be all here

    

    # for user in models.User.objects.all():
    #     Token.objects.get_or_create(user=user)
    
    # permission_classes = (permissions.UpdateOwnProfile,)
    # def get(self, request, format=None):
    #     content = {
    #         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': unicode(request.auth),  # None
    #     }
    #     return Response(content)
    # @api_view(['GET'])
    # def api_root(request, format=None):
    #     return Response({
    #         'users': reverse('user-list', request=request, format=format),
    #     })
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
    
# class LoginViewSet(mixins.ListModelMixin,
#                      viewsets.GenericViewSet):
                     
#     # permission_classes = [permissions.IsAuthenticated]
#     serializer_class = serializers.LoginSerializer
#     queryset = models.User.objects.all()
#     # def post(self,request):
#     #     data = request.data
#     #     username= data.get('email',)
#     #     password= data.get('password',)
#     #     user = auth.authenticate(username=username,password=password)
#     #     # print(user)
        
#     #     if user:
            
#     #         auth_token = jwt.encode(
#     #             {'username': user.email}, settings.JWT_SECRET_KEY)

#     #         serializer = UserProfileSerializer(user)

#     #         data = {'username': serializer.data, 'token': auth_token}

#     #         return Response(data, status=status.HTTP_200_OK)

#     #         # SEND RES
#     #     return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#     #     pass

#     # def post(self, request, *args, **kwargs):
#     #     serializer = self.serializer_class(data=request.data,
#     #                                        context={'request': request})
#     #     serializer.is_valid(raise_exception=True)
#     #     user = serializer.validated_data['email']
#     #     token, created = Token.objects.get_or_create(user=user)
#     #     return Response({
#     #         'token': token.key,
#     #         # 'name': user.pk,
#     #         'email': user.email
#     #     })
#     # 
#     # def create(self,request):
#     #     data = request.data
#     #     username= data.get('email',)
#     #     password= data.get('password',)
#     #     user = auth.authenticate(username=username,password=password)
#     #     print(user)
    
#     def create(self, request, format=None):
#         content = {
#             'email': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
   
   
# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })

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
    
    
    # @action(detail=False,methods=['GET'])
    # def view(self,request,pk=None):
    #     user=request.user.filter(user.emp_name)
    #     serializer=serializers.AttendanceSerializer(user)
    #     return Response(serializer.data, status=200)

    @action(detail=False, methods=['GET'])
    # def view(self, request, **kwargs):
    #     # filter_backends = [DjangoFilterBackend]
        # filterset_fields = ['emp_name']
    
        # user=request.user.filter('emp_name')
        # serializer = serializers.AttendanceSerializer(user, many=True) 
        # return Response(serializer.data)

    def view(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(emp_name=request.user)
        serializer = serializers.AttendanceSerializer(queryset, many=True) 
        return Response(serializer.data)
      
    def perform_create(self, serializer):
        # queryset = models.Attendance.objects.filter(emp_name=self.request.emp_name)
        

        serializer.save(emp_name=self.request.user)

class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset=models.LeaveType.objects.all()
    serializer_class=serializers.LeaveTypeSerializer
    
    
    
 
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
            

        # import pdb; pdb.set_trace()  
        serializer.data        
        e_subject = "Leave Verification"
        e_msg = "Here are the details about the leave\n"+"User Name:"+user.employee.username+"\n"+"Ëmail:"+user.employee.email+"\n"+"start date:"+str(user.start)+"\n"+"End date:"+str(user.end)+"\n"+"Number of days:"+str(user.number_of_days)+"\n"+"Reason:"+user.reason+"Verify:"+"http://127.0.0.1:8000/api/leave/"+str(user.id)
        e_mail = settings.EMAIL_HOST_USER
        Email=user.employee.email

        send_mail(
            e_subject,
            e_msg,
            e_mail,
            ['sunilshresthashrestha@gmail.com']
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
                Email=user.employee.email

                send_mail(
                    e_subject,
                    e_msg,
                    e_mail,
                    ['sunilsta010@gmail.com']

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
        user=request.user
        queryset = self.filter_queryset(self.get_queryset()).filter(user)
        serializer =serializers.MyLeaveSerializer(queryset,many=True)
        return Response(serializer.data)

class RemainingLeaveApiView(viewsets.ModelViewSet):
    # queryset = MyLeave.objects.all()
    
    serializer_class = serializers.MyLeaveSerializer
    
    queryset = models.MyLeave.objects.all() 

        # serializer = serializers.MyLeaveSerializer(queryset, many=True)
        # # import pdb;pdb.set_trace()
        # return Response(serializer.data)
                      
class SalaryReportApiView(viewsets.ModelViewSet):
    """Handli ccreating, updating salary field"""
    queryset = models.Salary.objects.all()
    serializer_class=serializers.SalaryReportSerializer
    permission_classes=[IsAdminUser]
    filter_backends=[DjangoFilterBackend,filterss.SearchFilter]
    filterset_fields=['amount','month','emp']
    search_fields=['^emp__email','^month','^emp__first_name','^emp__last_name','^year']
    


    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset=models.Salary.objects.all().order_by('-received_date')
            return queryset
        

        queryset = self.queryset
        query_set=queryset.filter(emp=self.request.user).order_by('-received_date')
        return query_set

    
    def get_permissions(self):
        if self.request.method=='GET':
            permission_classes=[IsAuthenticated,]
        else:
            permission_classes=[IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False,methods=['GET'],permission_classes=[IsAuthenticated])
    def salary_report(self,request):
        user=request.user
        salary =models.Salary.objects.filter(emp=user)
        serializer =serializers.SalaryReportSerializer(salary,many=True)
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



    
