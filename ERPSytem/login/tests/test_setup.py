from rest_framework.test import APITestCase,APIClient
from django.urls import reverse
from faker import Faker
from rest_framework_simplejwt import tokens
from login.serializers import LoginSerializer
from login.views import LoginAPIView,UserProfileViewSet
from requests import Response

class TestSetUp(APITestCase):

    def setUp(self):
        
        self.register_url=reverse('register')
        self.login_url=reverse('login')
        self.attendance_url='/api/attendance/'
        self.fake=Faker()
        
       
        

        self.user_data={
            
            'username':self.fake.email().split('@')[0],
            'email':self.fake.email(),
            'password':self.fake.email(),
            'first_name':self.fake.email().split('@')[0],
            'last_name':self.fake.email().split('@')[0],
            'address':self.fake.address(),
            'phone_number':self.fake.random_number(),
            'date_joined':self.fake.date(),
            'department':self.fake.email().split('@')[0],
            # 'document':"http://127.0.0.1:8000/media/media/AI.pdf",
            # 'photo':"http://127.0.0.1:8000/media/media/322868_1100-1100x628_x5HskII.jpg",
            
        }
        self.login_data={
    "email": "owner@owner.owner",
    # "username": "owner",
    # "tokens": {
    #     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMTcyNzE5OCwianRpIjoiMzk2ZjUwZDU4ZWM1NDFmY2JkZjhjNzY1ZDlhYTY1ZDciLCJ1c2VyX2lkIjoxNH0.gYu7PKTUemyDePXKNYxS5ErJ9nkKkObJT-cQZe-07rs",
    #     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExNjUyNzk4LCJqdGkiOiI1ODZmY2VlOGIwOTU0ZjFjODc1ZmIzYzc3Y2U1YjNmNyIsInVzZXJfaWQiOjE0fQ.NaTz_i_cFKGDcQVj4ME-AZlGnYzM7ZENCaQ6Z3QSRuE"
    # },
    # "is_superuser": False
}
        
#         # import pdb; pdb.set_trace()

        
        # serializer =LoginSerializer()
        # self.view=UserProfileViewSet()
        # self.login = LoginAPIView()
        # import pdb; pdb.set_trace()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
        


    
    
