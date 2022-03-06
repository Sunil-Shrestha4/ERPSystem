from django.urls import reverse
# from faker import Faker
from login.serializers import LoginSerializer, SalaryReportSerializer
from login.views import LoginAPIView, SalaryReportApiView, UserProfileViewSet
from requests import Response
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt import tokens
from rest_framework.authtoken.models import Token

# class TestSetUp(APITestCase):

#     def setUp(self):
        
#         self.register_url=reverse('register')
#         self.login_url=reverse('login')
#         self.attendance_url='/api/attendance/'
#         # self.fake=Faker()
        
       
        

#         self.user_data={
            
#             'username':self.fake.email().split('@')[0],
#             'email':self.fake.email(),
#             'password':self.fake.email(),
#             'first_name':self.fake.email().split('@')[0],
#             'last_name':self.fake.email().split('@')[0],
#             'address':self.fake.address(),
#             'phone_number':self.fake.random_number(),
#             'date_joined':self.fake.date(),
#             'department':self.fake.email().split('@')[0],
#             # 'document':"http://127.0.0.1:8000/media/media/AI.pdf",
#             # 'photo':"http://127.0.0.1:8000/media/media/322868_1100-1100x628_x5HskII.jpg",
            
#         }
#         self.login_data={
#     "email": "owner@owner.owner",
    # "username": "owner",
    # "tokens": {
    #     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMTcyNzE5OCwianRpIjoiMzk2ZjUwZDU4ZWM1NDFmY2JkZjhjNzY1ZDlhYTY1ZDciLCJ1c2VyX2lkIjoxNH0.gYu7PKTUemyDePXKNYxS5ErJ9nkKkObJT-cQZe-07rs",
    #     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExNjUyNzk4LCJqdGkiOiI1ODZmY2VlOGIwOTU0ZjFjODc1ZmIzYzc3Y2U1YjNmNyIsInVzZXJfaWQiOjE0fQ.NaTz_i_cFKGDcQVj4ME-AZlGnYzM7ZENCaQ6Z3QSRuE"
    # },
    # "is_superuser": False
# }
        
#         # import pdb; pdb.set_trace()

        
        # serializer =LoginSerializer()
        # self.view=UserProfileViewSet()
        # self.login = LoginAPIView()
        # import pdb; pdb.set_trace()
    #     return super().setUp()

    # def tearDown(self):
    #     return super().tearDown()
        


class SalaryTestSetUp(APITestCase):

    def setUp(self):
        self.login_url = reverse('login')
        self.salary_url = reverse('salary-list')
        # self.fake=Faker()
       
        self.admin_user = {
            "email" : "bmrsbhandari@gmail.com",
            # "username": "bmrsb51",
            "password":"bmrsb51",
            # "tokens": {
            #         "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMzEyNDM5MywianRpIjoiOTMwNTQ4MzZkNDI4NDNmOGJiYTE2Y2RmOWI0MDI0YzAiLCJ1c2VyX2lkIjoxfQ.olPXd-SxFfUy3AkzVoApoo15OyidKPZPuIuo73PDmJs",
            #         "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjEzMDQ5OTkzLCJqdGkiOiIwOGM3Njc1MTY3YTc0NmI0ODZkNDUxNTgzZmZlZGNkZSIsInVzZXJfaWQiOjF9.5xDH-TagxzzR9N8rRr3YWFbdZUN2ep_qZZjrQpWfngE"
            #     },
            # "is_superuser": "true",
            # "is_manager": "false"
        }
        self.nonAdmin_login_data={
            "email":"hello@gmail.com",
            "password":"bmrsb51",
            "is_manager": "false"
        }
        self.salary_data = {
            "amount": "134.00",
            "emp": 3,
            "allowance": "15.55",
            "year": "2020",
            "month": "april",
            "received_date": "2020-06-11"
        }
        self.salary_data2 = {
            "amount": "134.00",
            "emp": 1,
            "allowance": "15.55",
            "year": "2020",
            "month": "april",
            "received_date": "2020-11-11"
        }
        self.token = Token.objects.create(user=self.admin_user)
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
