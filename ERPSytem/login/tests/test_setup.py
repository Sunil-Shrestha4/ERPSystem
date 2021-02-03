# from rest_framework.test import APITestCase
# from django.urls import reverse
# from login.serializers import UserLeaveSerializer,LoginSerializer
# # from .models import User

# class TestSetUp(APITestCase):
    


#     def setUp(self):
#         # self.user = User(email="pop@gamil.com") 
#         # password = 's716751'
#         # self.user.set_password(password)
#         # self.user.save()

#         # self.client = Client()
#         # self.client.login(email=self.user.email, password=password)


#         self.leave_url='http://127.0.0.1:8000/api/leave/'
#         self.login_url=reverse('login')

#         self.user_leave={
#         "id": 1160,
#         "is_approved": False,
#         "is_notapproved": False,
#         "is_verified": False,
#         "is_notverified": False,
#         "start": "2021-01-19",
#         "end": "2021-01-20",
#         "number_of_days": 1,
#         "reason": "kjlkjlk",
#         "name": "admin",
#         "email": "admin@gmail.com"
#     }
#         self.login_data={
#     "email": "admin@gmail.com",

#     "password":"s716751",
#     # "tokens": {
#     #     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMTc0NTM2NSwianRpIjoiNzU0MDk4MGE5ZGMwNDlhM2JmM2Y0Yzk2MGE0NWZkNGEiLCJ1c2VyX2lkIjoxfQ.N3e6M3nI0_hz2o0EuxE9DnzKcWeVZvMQeLSKEh7PG6I",
#     #     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExNjcwOTY1LCJqdGkiOiIwNmQ5ZGNkYzIwM2Q0YjI4YjdiZGQ1MzFjNTQ4Y2VlYiIsInVzZXJfaWQiOjF9.q7EBkd0tYnT0BHzNaPlQHKrcaKp_9elYS4Y1YGtqTKY"
#     # },
#     # "is_superuser": True,
#     # "is_manager": True
# }
        
#         self.serializer=UserLeaveSerializer()
#         self.login=LoginSerializer()
#         import pdb
#         pdb.set_trace()


#         return super().setUp()

#     def tearDown(self):
#         return super().tearDown()







