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
from .serializers import RegisterSerializer,EmailVerificationSerializer

from rest_framework import generics, status, views, permissions
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .utils import Util , EmailThread
from django.urls import reverse
import jwt
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings



class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

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
    # permission_classes = [permissions.IsAuthenticated , permissions.IsAdminUser]


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
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
    serializer_class = serializers.DeptSerializer
    queryset = models.Department.objects.all()
    # permission_classes = [permissions.IsAdminUser]

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AttendanceSerializer
    queryset = models.Attendance.objects.all()
    # permission_classes = [permissions.IsAuthenticated ]
    

class RegisterViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.RegisterSerializer
    queryset = models.User.objects.all()

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     return Response({
    #     "user": UserProfileSerializer(user, context=self.get_serializer_context()).data,
    #     "token": AuthToken.objects.create(user)[1]

    #     })
    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data =serializer.data
        user = User.objects.get(email=user_data['email'])
        token =RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink=reverse('email-verify')
    
        absurl ='http://'+current_site+relativeLink+"?token="+str(token)
        email_body='HI '+user.username+'Use link below to verify ypur email \n'+absurl
        data ={'email_body':email_body,'to_email':user.email, 'email_subject':'Verify your email'}
        Util.send_email(data)
        return Response(user_data,status=status.HTTP_201_CREATED)

# class VerifyEmail(viewsets.ModelViewSet):
#     ''


    
 
class LeaveViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.LeaveSerializer
    queryset = models.Leave.objects.all()   
  
   
class SalaryReportApiView(viewsets.ModelViewSet):
    """Handli ccreating, updating salary field"""
    serializer_class = serializers.SalaryReportSerializer 
    queryset = models.Salary.objects.all()
    # permission_classes = [permissions.IsAuthenticated ]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
