# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """ Create new user profile"""
        if not email:
            raise ValueError('USer must have email address')
        
        email = self.normalize_email(email)
        user =self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,name,password):
        """Create and save a new super user with given details"""
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email =models.EmailField(max_length=225,unique=True)
    name =models.CharField(max_length=225)
    is_active=models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrive short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
    

class RegisterUser(models.Model):
    """Database model for users in the system"""
    emp_id=models.IntegerField()
    email =models.EmailField(max_length=225,unique=True)
    first_name =models.CharField(max_length=225)
    last_name =models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    phone_number=PhoneNumberField(null=False, blank=False, unique=True)
    position=models.CharField(max_length=225)
    department=models.CharField(max_length=225)
    is_active=models.BooleanField(default=True)
    is_staff =models.BooleanField(default=True)
    file = models.ImageField(upload_to='pics', blank=True)

    def __str__(self):
        return self.first_name

class Leave(models.Model):
    emp_id=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    leave_status=models.BooleanField(default=False)
    number_of_days=models.IntegerField(default=0)
    emp_name=models.CharField(max_length=225)
    reason=models.TextField(max_length=500, blank=False)
    

    def __str__(self):
        return self.emp_name

