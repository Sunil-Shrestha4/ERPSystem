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



class HelloApiView(APIView):

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
    authentication_classes = (TokenAuthentication,BasicAuthentication,SessionAuthentication)
    permission_classes = [permissions.IsAuthenticated  , permissions.IsAdminUser]


# class UserLoginApiView(ObtainAuthToken):
    

#    """Handle creating user authentication tokens"""
#    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class RegisterViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.RegisterSerializer
    queryset = models.RegisterUser.objects.all()

    def perform_create(self, serializer):
        created_object = serializer.save()
        send_mail('User Profile created','You have sucessfully register','sunilsta010@gmail.com', 
            [created_object.email],  fail_silently=False,)

class LeaveViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.LeaveSerializer
    queryset = models.Leave.objects.all()
   
   