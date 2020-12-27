from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from login import serializers
from rest_framework import viewsets
from login import models
from rest_framework.authentication import TokenAuthentication
from login import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings





    """ Test API View """
    # serializer_class = serializers.HelloSerailizer


    def get(self, request,format=None):
        """"Returns a list of APIVIew features"""
        an_apiview=[
            'Uses Http as function (get,post,patch, delete)'
            'Is similar to traditional django view',
            
        ]

        return Response({'message':'Hello0','an_apiview':an_apiview})

    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """ Handle updating object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCh'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


# class HelloViewSet(viewsets.ViewSet):
#     """Test API viewset"""

#     def list(self,reqiuest):
#         """Return a hello message"""

#         a_viewset=[
#             'Uses action (list,create,retrieve, update,partial_update)',
#             'Automatically maps  to a URLs Using Routers',
#             'Provides more functionality with less code'

        




#         ]
#         return Response({'message':'Hello','a_viewset':a_viewset})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    

   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class DeptViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeptSerializer
    queryset = models.Department.objects.all()

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AttendanceSerializer
    queryset = models.Attendance.objects.all()
    # if models.Attendance.objects.filter(checkin == True):
    #     return 
    # else :
    #     return

    # def get(self, request):
        

    
   
  
   
class SalaryReportApiView(viewsets.ModelViewSet):
    """Handli ccreating, updating salary field"""
    serializer_class = serializers.SalaryReportSerializer
    queryset = models.User.objects.all()

class RegisterViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.RegisterSerializer
    queryset = models.RegisterUser.objects.all()

class LeaveViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.LeaveSerializer
    queryset = models.Leave.objects.all()
   
   
