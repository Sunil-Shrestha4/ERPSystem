# from .test_setup import TestSetUp
# from rest_framework.test import force_authenticate
# class TestViews(TestSetUp):
#     def test_user_cannot_takeleave_with_no_data(self):
#         res=self.client.post(self.leave_url)
#         # import pdb
#         # pdb.set_trace()
#         self.assertEqual(res.status_code,401)

#     def test_user_can_takeleave_with_all_data(self):
#         import pdb
#         pdb.set_trace()

#         ram=self.client.post(self.login_url,self.login_data,format="json")
        

#         res=self.client.post(self.leave_url,self.user_leave,format="json")
#         # client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json()['access_token'])
#         import pdb
#         pdb.set_trace()
#         # user = User.objects.get(username='olivia')
#         # request = factory.get('/accounts/django-superstars/')
#         # force_authenticate(request, user=user, token=user.auth_token)
#         self.assertEqual(res.status_code,201)
    

    

