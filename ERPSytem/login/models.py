# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from djmoney.models.fields import MoneyField


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
    created = models.DateTimeField(auto_now_add=True)
    
    is_active=models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)
    # salary=models.PositiveIntegerField(_("salary"))
    
    

    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    
    # def get_short_name(self):
    #     """Retrive short name of user"""
    #     return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.name
    class Meta:
        ordering = ['created']
    
class Login(models.Model) :
     email=models.ForeignKey(User,on_delete=models.CASCADE)
     



class Department(models.Model):
    #   users =models.ForeignKey(User, on_delete=models.CASCADE, default=0)
      dept_name = models.CharField(max_length=30)

      def __str__(self):
        """Return string representation of user"""
        return self.dept_name

    
      
    
class Attendance(models.Model):
    emp_name = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    TYPE = (
        ('CI', 'checkin'),
        ('CO', 'checkout'),
    )
    choices = models.CharField(max_length=2, choices=TYPE,default='checkin')
        

    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choices
    
    
    
    # if checkin ==False:
    #     checkin = models.DateTimeField(null=True)
    # else: pass
    # checkout = models.DateTimeField(auto_now_add=True)
    
    
    # class Meta:
    #     ordering = ['checkin','checkout']


class Salary(models.Model):
    employee_name = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    amount =  MoneyField(max_digits=14, decimal_places=2, default_currency='NPR')
    department =models.ForeignKey(Department,on_delete=models.CASCADE,default=0)

