from .test_setup import TestSetUp
from ..models import User
from rest_framework.test import force_authenticate
from requests import Response
from rest_framework_simplejwt import tokens


class TestViews(TestSetUp):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        # import pdb; pdb.set_trace()
        
        self.assertEqual(res.status_code,400)
    
    def test_user_can_register_correctly(self):
        self.client.post(self.login_url,self.login_data,format="json")
        # import pdb; pdb.set_trace()
        
        # import pdb; pdb.set_trace()
        # request = self.client.get(self.register_url,format="json")
        # force_authenticate(request, user=user,token=None)
        # res = view(request)
        # import pdb; pdb.set_trace()
        res=self.client.post(self.register_url,self.user_data,format="json")
        
        # import pdb; pdb.set_trace()
        # import pdb; pdb.set_trace()
        # force_authenticate(res, user=user, token=None)
        # res = self.client.post(self.register_url,self.user_data,format="json")
        
        # import pdb; pdb.set_trace()
        self.assertEqual(res.status_code,201)

    def test_login_with_unverified_user(self):
        
        self.client.post(self.register_url,self.user_data,format="json")
        
        user = User.objects.get(email=self.user_data['email'])
        user.save()
        # import pdb; pdb.set_trace()
        # data=self.serializer.validate(True)
        # import pdb; pdb.set_trace()
        
        # data.save()
        

        res=self.client.post(self.login_url,format="json")
        # import pdb; pdb.set_trace()
        self.assertEqual(res.status_code,401)

    def test_login_with_verified_user(self):
        self.client.post(self.register_url,self.user_data,format="json")
        # import pdb; pdb.set_trace()
        user = User.objects.get(email=self.user_data['email'])
        user.is_valid=True
        user.is_verified=True
        user.save()
        res=self.client.post(self.login_url,self.user_data,format="json")
        # import pdb; pdb.set_trace()
        self.assertEqual(res.status_code,200)

    


        
