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



   
        

    @action(detail=False,methods=['GET'],permission_classes = [IsAssigned,])
    def viewuserdetail(self,request,pk=None):
        # import pdb;pdb.set_trace()
        user=request.user
        serializer=serializers.UserDetailSerializer(user)
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
    permission_classes = [permissions.IsAdminUser,]
    serializer_class = serializers.DeptSerializer
    queryset = models.Department.objects.all()
    # permission_classes = [permissions.IsAdminUser]

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AttendanceSerializer
    queryset = models.Attendance.objects.all()
    permission_classes = [permissions.IsAuthenticated ]
     
    # def post(self,request):
    #      user = request.data
    #      serializer = self.serializer(data=user)
    #      try:
    #         serializer.is_valid(raise_exception=True)
    #         user = serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #      except:
    #         return Response(serializer.data , status=status.HTTP_401_UNAUTHORIZED)
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        # queryset = models.Attendance.objects.filter(emp_name=self.request.emp_name)
        

        serializer.save(emp_name=self.request.user)
    # def get_permissions(self):
    
    #     if self.request.method == 'GET':
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]


    
    





    
 
class LeaveViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.LeaveSerializer
    queryset = models.Leave.objects.all() 
    permission_classes = [permissions.IsAuthenticated ]
     
  
   
class SalaryReportApiView(viewsets.ModelViewSet):
    """Handli ccreating, updating salary field"""
    serializer_class = serializers.SalaryReportSerializer 
    queryset = models.Salary.objects.all()
    # 
    permission_classes = [permissions.IsAdminUser] 

    def perform_create(self, serializer):
        # queryset = models.Attendance.objects.filter(emp_name=self.request.emp_name)
        

        serializer.save(employee_name=self.request.user)

    # def get(self, request, format=None):
    #     salary = Salary.objects.all()
    #     serializer = SalaryReportSerializer(salary,many=True)
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return JSONResponse(serializer.data,safe= False)
    
    # def post(self,request):
    #     data = JSONParser().parse(request)
    #     serializer=self.get_serializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)








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



    # def get(self, request, format=None):
    #     userdetails = UserDetails.objects.all()
    #     serializer = UserDetailSerializer(userdetails, many=True)
    #     return Response(serializer.data)


     
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




    @action(detail=False,methods=['GET'],permission_classes = [IsAssigned,])
    def userdetail(self,request,pk=None):
        user=request.user
        serializer=serializers.UserDetailSerializer(user)
        return Response(serializer.data, status=200)


    
