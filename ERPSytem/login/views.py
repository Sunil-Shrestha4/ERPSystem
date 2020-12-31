from rest_framework.views import APIView
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

from .utils import Util
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





class LeaveViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.LeaveSerializer
    queryset = models.Leave.objects.all()
   
   