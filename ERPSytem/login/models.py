# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
import datetime as dt

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

    # def create_user(self,email,username,password=None):
    #     """ Create new user profile"""

    #     if not email:
    #         raise ValueError('USer must have email address')
        
    #     email = self.normalize_email(email)
    #     user =self.model(email=email,username=username)


    #     user.set_password(password)
    #     user.save(using=self._db)
        

class UserProfileManager(BaseUserManager):

    def create_user(self, username, email,first_name,last_name,address,phone_number,position,date_joined,department,document,photo,password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username,first_name=first_name,last_name=last_name,address=address,phone_number=phone_number,date_joined=date_joined,department=department,document=document,photo=photo, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    # def create_user(self, username, email, password=None):
    #    if username is None:
    #        raise TypeError('Users should have a username')
    #    if email is None:
    #        raise TypeError('Users should have a Email')
 
    #    # user = self.model(username=username,first_name=first_name,last_name=last_name,address=address,phone_number=phone_number,date_joined=date_joined,department=department,document=document,photo=photo, email=self.normalize_email(email))
    #    user = self.model(username=username, email=self.normalize_email(email))
    #    user.set_password(password)
    #    user.save()
    #    return user
   

    def create_superuser(self, username, email, password):
        """Create and save a new super user with given details"""
        user=self.create_user(username, email, password)
    # def create_superuser(self, username, email, password=None):
    #     if password is None:
    #         raise TypeError('Password should not be none')

        # user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}

class Department(models.Model):
    #users =models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    # DEPT_NAMES = (
    #     ('IT', 'IT'),
    #     ('SD', "sadd"),
    #     ('HHJ', "hjjj"),
    #     ('DEN', "daat"),
    #     ('ADMIN', "administration"),
    #     ('STF', "staff"),
    # )
    dept_name = models.CharField(max_length=30)

    def __str__(self):
        return self.dept_name

class User(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email =models.EmailField(max_length=225,unique=True,db_index=True)
    username =models.CharField(max_length=225,db_index=True)
    password=models.CharField(max_length=225,default=1234)
    first_name =models.CharField(max_length=225,default='abc')
    last_name =models.CharField(max_length=225,default='abc')
    address=models.CharField(max_length=225,default='abc')
    phone_number=models.IntegerField(null=True, blank=True)
    position=models.CharField(max_length=225,default='Trainee')
    date_joined=models.DateField(null=True)
    department=models.CharField(max_length=225)
    document = models.FileField(upload_to='media', blank=True)
    photo = models.ImageField(upload_to='media', blank=True)
    is_verified = models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    # salary=models.PositiveIntegerField(_("salary"))
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['username']

    objects = UserProfileManager()

    def get_full_name(self):
        """Retrive full name of user"""
        return self.username
    
    # def get_short_name(self):
    #     """Retrive short name of user"""
    #     return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.username
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh) ,
            'access':str(refresh.access_token)


        }

    class Meta:
        ordering = ['created_at']
    
# class Login(models.Model) :
#      email=models.ForeignKey(User,on_delete=models.CASCADE)
#      password = models.CharField(max_length=50)
     



# class Department(models.Model):
#     #   users =models.ForeignKey(User, on_delete=models.CASCADE, default=0)
#       dept_name = models.CharField(max_length=30)

#       def __str__(self):
#         """Return string representation of user"""
#         return self.dept_name

    
      
    
class Attendance(models.Model):
    emp_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    TYPE = (
        ('CI', 'checkin'),
        ('CO', 'checkout'),
    )
    # choices = models.CharField(max_length=2, choices=TYPE,default='checkin')
    checkin = models.BooleanField(default=False)
    checkout = models.BooleanField(default=False)    
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return "Checkin: "+str(self.checkin)+" Checkout: "+str(self.checkout)
    



class Salary(models.Model):
    amount =  MoneyField(max_digits=14, decimal_places=2, default_currency='NPR', default=0)
    emp=models.ForeignKey(User,on_delete=models.CASCADE)
    allowance = MoneyField(max_digits=14, decimal_places=2, default_currency='NPR', default=0)
    month = models.CharField(max_length=225, default=0)
    received_date = models.DateField(default=dt.date.today)

    def __str__(self):
       return str(self.emp.username)+str(self.amount)
    

class UserDetails(models.Model):
    """Database model for users in the system"""
    
    username =models.CharField(max_length=225,db_index=True,unique=True)
    email =models.EmailField(max_length=225,unique=True)
    password=models.CharField(max_length=225,default=1234)
    first_name =models.CharField(max_length=225)
    last_name =models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    phone_number=models.IntegerField(null=True, blank=False, unique=True)
    position=models.CharField(max_length=225)
    date_joined=models.DateField(auto_now_add=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE, max_length=225)
    is_active=models.BooleanField(default=True)
    is_staff =models.BooleanField(default=True)
    document = models.FileField(upload_to='pics', blank=True)
    photo = models.ImageField(upload_to='pics', blank=True)


    def __str__(self):
        return self.first_name

class Leave(models.Model):
    emp_id=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    leave_status=models.BooleanField(default=False)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    number_of_days=models.IntegerField(default=0)
    emp_name=models.CharField(max_length=225)
    reason=models.TextField(max_length=500, blank=False)
    

    def __str__(self):
        return self.emp_name