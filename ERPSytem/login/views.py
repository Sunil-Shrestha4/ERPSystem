from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from login import serializers
from rest_framework import viewsets
from login import models
from rest_framework.authentication import TokenAuthentication
# from login import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token





class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated , permissions.IsAdminUser]
    # for user in models.User.objects.all():
    #     Token.objects.get_or_create(user=user)
    
    # permission_classes = (permissions.UpdateOwnProfile,)
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
    @api_view(['GET'])
    def api_root(request, format=None):
        return Response({
            'users': reverse('user-list', request=request, format=format),
        })
    


# class UserLoginApiView(viewsets.ModelViewSet):
    
#     queryset = models.User.objects.all()
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
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
   
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
    permission_classes = [permissions.IsAdminUser]

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AttendanceSerializer
    queryset = models.Attendance.objects.all()
    permission_classes = [permissions.IsAuthenticated ]
    # if models.Attendance.objects.filter(checkin == True):
    #     return 
    # else :
    #     return

    # def get(self, request):
        

    

class RegisterViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.RegisterSerializer
    queryset = models.RegisterUser.objects.all()

class LeaveViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.LeaveSerializer
    queryset = models.Leave.objects.all()   
  
   
class SalaryReportApiView(viewsets.ModelViewSet):
    """Handli ccreating, updating salary field"""
    serializer_class = serializers.SalaryReportSerializer
    queryset = models.Salary.objects.filter( pk = 1 )
    permission_classes = [permissions.IsAuthenticated ]
